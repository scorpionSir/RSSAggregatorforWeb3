import sys
sys.path.append('../')
import media_lib as ml
import lxml
from dateutil import parser
from tqdm import tqdm
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
        self.channel_scheduler = ml.ChannelScheduler('web3', self.channel.id)
        self.logger = ml.logger

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
                await ml.TtRssFeed.create(url=feed_dict['href'], updated=updated, title=feed['title'], subtitle=subtitle)
        print('finished')

    async def sync_feed(self, db_feed: ml.TtRssFeed):
        feed_dict = await self.feed_parser.parse(db_feed.url)
        if not feed_dict:
            self.logger.info(f'Can not get the content from db_feed {repr(db_feed)}')
            return
        feed = feed_dict['feed']
        updated = feed['updated'] if 'updated' in feed_dict['feed'] else feed_dict['entries'][0]['published']
        updated = parser.parse(updated).timestamp()
        if updated <= db_feed.updated:
            return
        entries = list()
        for entry in feed_dict['entries']:
            published = entry['published'] if 'published' in entry else entry['updated']
            published = parser.parse(published)
            if published.timestamp() > db_feed.updated:
                entries.append((entry, published))
            else:
                break
        entries = sorted(entries, key=lambda x: x[1])
        results = list()
        for entry, published in entries:
            res = await self.send_entry(entry, str(published))
            if not res:
                self.logger.info(f"Error in send_entry for the db_seed {repr(db_feed)}")
                return
            results.append(res)
            db_feed.updated = published.timestamp()
            await db_feed.save()
        return results

    async def sync(self):
        db_feeds = await ml.TtRssFeed.all()
        sync_time = await ml.TtDict.get_or_none(key="web3_rss_sync_time")
        if not sync_time:
            sync_time = parser.parse('2021-07-08T07:00:34Z').timestamp()
            await ml.TtDict.create(key='web3_rss_sync_time', value=str(sync_time))
        else:
            sync_time = float(sync_time.value)
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

        for idx, entry in enumerate(tqdm(entries)):
            published = entry['published'] if 'published' in entry else entry['updated']
            pub_time = parser.parse(published).timestamp()
            if pub_time <= sync_time:
                continue
            print(f'sync the {idx} entry')
            res = await self.send_entry(entry)
            # if not res:
            #     raise RuntimeError()
        print('finished')

    async def initial_sync(self, sync_time_str: str=None):
        db_feeds = await ml.TtRssFeed.all()
        if sync_time_str:
            sync_time = parser.parse(sync_time_str).timestamp()
            db_sync_time = await ml.TtDict.get_or_none(key="web3_rss_sync_time")
            if db_sync_time:
                db_sync_time.value = str(sync_time)
                await db_sync_time.save()
            else:
                await ml.TtDict.create(key='web3_rss_sync_time', value=str(sync_time))
        else:
            db_sync_time = await ml.TtDict.get_or_none(key="web3_rss_sync_time")
            if db_sync_time:
                sync_time = float(db_sync_time.value)
            else:
                sync_time = 0.
                await ml.TtDict.create(key='web3_rss_sync_time', value=str(sync_time))

        entry_file = self.work_dir.joinpath('entries.pk')
        if not entry_file.exists():

            async def get_feed_dict(db_feed):
                return await self.feed_parser.parse(db_feed.url)

            aio_queue = ml.AioQueue(15, get_feed_dict, key_arg=0)
            await aio_queue.run(db_feeds)
            entries = list()
            for url, feed_dict in aio_queue.results.items():
                if not feed_dict:
                    continue
                entries.extend(feed_dict['entries'])
            entries = sorted(entries, key=lambda x: parser.parse(x['published'] if 'published' in x else x['updated']).timestamp())
            pickle.dump(entries, entry_file.open('wb'))
        else:
            entries = pickle.load(entry_file.open('rb'))

        for idx, entry in enumerate(tqdm(entries)):
            published = entry['published'] if 'published' in entry else entry['updated']
            pub_time = parser.parse(published)
            if pub_time.timestamp() <= sync_time:
                continue
            print(f'sync the {idx} entry')
            res = await self.send_entry(entry, str(pub_time))
            if not res:
                raise RuntimeError()
        print('finished')

    async def send_entry(self, entry, published=None):
        if 'tags' in entry:
            tags = [f"#{item['term'].replace('-', '_')}  " for item in entry['tags']]
            tags = ''.join(tags)
        else:
            tags = None
        if not published:
            published = entry['published'] if 'published' in entry else entry['updated']
            published = str(parser.parse(published))
        text = (f"""**Title:** {entry['title']} \n\n**Tags:** {tags} \n\n"""
                f"""**Published:** {published} \n\n**Created by:** @scorpion_media_bot \n\n"""
                f"""**Link:** {entry['link']}"""
                )
        chat_id = await self.channel_scheduler.get_chat_id()
        ret = await self.bot.api.send_message(chat_id, text, parse_mode='markdown')
        return ret


channel = Web3Channel()
ml.async_run(channel.sync())
























