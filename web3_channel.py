import sys
sys.path.append('../')
import media_lib as ml
import lxml
import os
from dateutil import parser
from tqdm import tqdm
import io
import markdownify
import html2text
from github import Github
import pickle


class Web3Channel(object):
    def __init__(self, work_dir='./web3_channel'):
        self.work_dir = ml.to_path(work_dir, try_create=True)
        self.proxy = ml.get_default_proxy()
        self.aio_http = ml.AioHttp(proxy=self.proxy)
        self.feed_parser = ml.FeedParser(proxy=self.proxy)
        self.sql = ml.get_default_tg_sql()
        self.cfg_sql = ml.get_default_cfg_sql()
        self.channel = self.cfg_sql.get_channel(tag='web3_rss')
        self.bot = ml.create_bot('scorpion_media_bot', work_dir=work_dir)
        self.github = Github('xx')
        self.repo = self.github.get_user().get_repo('RSSAggregatorforWeb3')
        self.db_files = self.repo.get_contents('md_files')
        self.db_file_names = [item.name for item in self.db_files]

    async def init_from_opml_file(self):
        opml_file = self.work_dir.joinpath('RAW.opml')
        tree = lxml.etree.parse(opml_file.as_posix())
        for sub_element in tree.findall('body/outline'):
            sub_urls = list()
            for element in sub_element.getchildren():
                db_feed = await ml.TtRssFeed.get_or_none(url=element.get('xmlUrl'))
                if db_feed:
                    continue
                sub_urls.append(element.get('xmlUrl'))
            aio_queue = ml.AioQueue(10, self.feed_parser.parse, key_arg=0)
            await aio_queue.run(sub_urls)
            feed_dicts = aio_queue.results
            for url, feed_dict in feed_dicts.items():
                if not feed_dict:
                    continue
                feed = feed_dict['feed']
                db_feed = await ml.TtRssFeed.get_or_none(url=feed_dict['href'])
                if db_feed:
                    continue
                try:
                    updated = feed['updated'] if 'updated' in feed else feed_dict['entries'][0]['published']
                except:
                    continue
                updated = parser.parse(updated).timestamp()
                subtitle = feed.get('subtitle', None)
                if subtitle and subtitle.startswith('<a class'):
                    subtitle = None
                await ml.TtRssFeed.create(url=feed_dict['href'], updated=updated, title=feed['title'],subtitle=subtitle)
        print('finished')

    async def sync_feed(self, db_feed: ml.TtRssFeed):
        feed_dict = await self.feed_parser.parse(db_feed.url)
        return feed_dict

    async def initial_sync(self):
        db_feeds = await ml.TtRssFeed.all()
        entry_file = self.work_dir.joinpath('entries.pk')
        if not entry_file.exists():
            aio_queue = ml.AioQueue(15, self.sync_feed, key_arg=0)
            await aio_queue.run(db_feeds)
            entries = list()
            for url, feed_dict in aio_queue.results.items():
                if not feed_dict:
                    continue
                entries.extend(feed_dict['entries'])
            entries = sorted(entries, key=lambda x: parser.parse(x['updated']).timestamp())
            pickle.dump(entries, entry_file.open('wb'))
        else:
            entries = pickle.load(entry_file.open('rb'))
        is_start = False
        # new_entries = list()
        # for item in entries:
        #     if not is_start and item['title'].startswith('Sale Delayed — New Date: Thursday Aug 10'):
        #         is_start = True
        #     if is_start:
        #         new_entries.append(item)
        channel_scheduler = ml.ChannelScheduler('web3', self.channel.id)
        for entry in entries:
            chat_id = await channel_scheduler.get_chat_id()
            res = await self.send_entry(entry, chat_id)
            if not res:
                raise RuntimeError()
        print('finished')

    async def send_entry(self, entry, chat_id):
        if 'tags' in entry:
            tags = [f"#{item['term'].replace('-', '_')}  " for item in entry['tags']]
            tags = ''.join(tags)
        else:
            tags = None
        res = await self.aio_http.request(entry['link'])
        if not res:
            raise RuntimeError
        _, html = res.value
        md = html2text.html2text(html.decode())
        md_name = entry['title'] + '.md'
        ret = self.repo.create_file(f"md_files/{md_name}", 'uploading md file', md, branch='main')
        md_link = ret['content'].html_url
        # if md_name not in self.db_file_names:
        #     ret = self.repo.create_file(f"md_files/{md_name}", 'uploading md file', md, branch='main')
        #     md_link = ret['content'].html_url
        # else:
        #     content = [item for item in self.db_files if item.name == md_name][0]
        #     md_link = content.html_url
        # md = io.BytesIO(md.encode())
        published = entry['published'] if 'published' in entry else entry['updated']
        text = (f"""**Title:** {entry['title']} \n\n**Tags:** {tags} \n\n"""
                f"""**Published:** {published} \n\n**Created by:** @scorpion_media_bot \n\n"""
                f"""**Original Link:** {entry['link']} \n\n"""
                f"""**Github Link:** {md_link}"""
                # f"""**Original Link:** {entry['link']}"""
                )
        return await self.bot.api.send_message(chat_id, text, parse_mode='markdown')


channel = Web3Channel()
ml.async_run(channel.initial_sync())
























