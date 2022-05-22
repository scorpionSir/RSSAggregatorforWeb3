[Go Back](../../)[Fleek.co](https://Fleek.co)

# How to deploy a Next.js app onto IPFS using Fleek

![](https://fleek-team-bucket.storage.fleek.co/thumbnails-blog/Next.png)

## Overview

We’ll create a Next.js app and deploy it on Fleek. This whole process should
take 10 minutes.

Tools:

  * Fleek account
  * GitHub account
  * node.js/npm

### Step 1: Set Up a Repo on Github

Create an empty repository and clone it.

[
![CreateRepo](../../static/f9b6940f61762295997a682ef981bbc3/d9199/CreateRepo.png)
](../../static/f9b6940f61762295997a682ef981bbc3/5bd27/CreateRepo.png)

Create a Next.js app using:

`$ mkdir nextjs && cd nextjs` `$ npm init --y' '$ npm install next react
react-dom`

[
![CreateNextjsapp](../../static/62587cc8140f76c8fd08d047013ba53a/d9199/CreateNextjsapp.png)
](../../static/62587cc8140f76c8fd08d047013ba53a/e2bb0/CreateNextjsapp.png)

Open `package.json` and add in the following scripts

    
    
    "scripts": {
        "dev": "next",
        "build": "next build",
        "start": "next start",
        "export": "next export"  
    }

[
![Openpackagejson](../../static/704369bd2e475cac41a8e5ff1f6c9d9a/d9199/Openpackagejson.png)
](../../static/704369bd2e475cac41a8e5ff1f6c9d9a/252a4/Openpackagejson.png)

Create a `next.config.js` file in the root directory

    
    
    module.exports = {
      exportTrailingSlash: true,
    };

[
![createNextConfigJS](../../static/bf3c3808069eb28f708d238e354e784c/d9199/createNextConfigJS.png)
](../../static/bf3c3808069eb28f708d238e354e784c/f32b7/createNextConfigJS.png)

Let’s create some pages: Create a folder called pages Inside pages, create
`index.js`

    
    
    // index.js
    import Link from "next/link";
    
    export default function Index() {
      return (
        <div>
          <h1> Index </h1>
          <Link href="/about">
            <a> About </a>
          </Link>
        </div>
      );
    }

and `about.js`

    
    
    // about.js
    export default function About() {
      return (
        <div>
          <h1> About </h1>
        </div>
      );
    }

It should look something like this

[
![indexJSAboutJS](../../static/e3e60d59ccb5e8946672bdc092945d12/d9199/indexJSAboutJS.png)
](../../static/e3e60d59ccb5e8946672bdc092945d12/53639/indexJSAboutJS.png)

To test, run `npm run dev` and visit localhost:3000

[
![localhost3000](../../static/47534d744fd9d586bd69b586d657b42f/d9199/localhost3000.png)
](../../static/47534d744fd9d586bd69b586d657b42f/78415/localhost3000.png)

git add, commit, push

[
![gitcommit](../../static/fd33e7b87e0f01ab592450457859d565/d9199/gitcommit.png)
](../../static/fd33e7b87e0f01ab592450457859d565/f663d/gitcommit.png)

### Step 2: Set Up Fleek

Sign into <https://app.fleek.co/>

Sign in with Github

[ ![signin](../../static/120c9c58e92b8db6675e28d3aa6bfe0f/d9199/signin.png)
](../../static/120c9c58e92b8db6675e28d3aa6bfe0f/c65fa/signin.png)

Add New Site

[ ![addsite](../../static/6f10fe25639ab703c85ffc979e23c453/d9199/addsite.png)
](../../static/6f10fe25639ab703c85ffc979e23c453/07a9c/addsite.png)

Connect with Github.

[
![connectGithub](../../static/f0d0a286428a0f157ab5979842ab22cc/d9199/connectGithub.png)
](../../static/f0d0a286428a0f157ab5979842ab22cc/07a9c/connectGithub.png)

Pick your Next.js repository.

[
![picknextjsrepo](../../static/01a5e7be49f1075306569df891256018/d9199/picknextjsrepo.png)
](../../static/01a5e7be49f1075306569df891256018/07a9c/picknextjsrepo.png)

To create a new site:

Build command: `npm install && npm run build && npm run export`

docker image: `fleek/next-js`

Publish directory: `out`

Of course, fleek will autodetect next-js and enter those configurations
automatically. :P

It’s worth noting that the docker image `fleek/next-js` runs the most recent
version of node.js by default, which, by the time of this writing, is version
13.

If you need to use another node version, you can do so via the docker tag. EG:
For node 10, use `fleek/next-js:node-10`

Deploy Site

[
![deploySite](../../static/6320ad97c61f1cd4073a646ca2f54474/d9199/deploySite.png)
](../../static/6320ad97c61f1cd4073a646ca2f54474/133ae/deploySite.png)

Once complete, view your website.

[
![viewSite](../../static/811ec898edf8739e26aa22e406ace7dd/d9199/viewSite.png)
](../../static/811ec898edf8739e26aa22e406ace7dd/91b67/viewSite.png)

You can view the website using the provided domain name.

`https://<your-domain>.on.fleek.co`

Or verify with the CID.

`https://ipfs.io/ipfs/<CID>`

[
![verifyCID](../../static/d68b4e4451a8bcd6481d442613aa17a4/d9199/verifyCID.png)
](../../static/d68b4e4451a8bcd6481d442613aa17a4/6fcb6/verifyCID.png)

### Step 3: Updates

Fleek will automatically redeploy your website whenever you make changes to
GitHub. Make sure to provide the domain name will remain the same and will
point to the new CID. This enables you to build fast modern websites hosted on
IPFS.

  * [Sign up](https://app.fleek.co) to try yourself
  * Join our [Community Chat](https://slack.fleek.co/)
  * Follow us on [Twitter](https://twitter.com/FleekHQ)
  * Check out our [Tech Docs](https://docs.fleek.co/)
  * Contact us at support@fleek.co

Published 12 Mar 2020

  * [Tutorial](../../tag/tutorial/)
  * [Guide](../../tag/guide/)

Fleek is all you need to build websites and apps on the new Open Web:
permissionless, trustless, censorship resistant, and free of centralized
gatekeepers. Welcome to the new internet.[](https://www.twitter.com/FleekHQ)

