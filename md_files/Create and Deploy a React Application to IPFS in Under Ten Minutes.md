[Go Back](../../)[Fleek.co](https://Fleek.co)

# Create and Deploy a React Application to IPFS in Under Ten Minutes

![](https://fleek-team-bucket.storage.fleek.co/thumbnails-
blog/CreateReactAppSocialimage.png)

A React application can be bootstrapped in a matter of minutes with create-
react-app. Fleek allows apps to be deployed to IPFS in a matter of minutes.
These two go together like peanut butter and jelly, allowing for development
and deployment to be complete in a flash.

We will do it in two steps which are: 1. Creating a react application with
create-react-app 2. Deploying our app to IPFS on Fleek. This process takes
less than ten minutes. Let’s go!

### Step 1: Creating a React application with create-react-app

Create-react-app requires npm => 5.6 and node >= 8.10, so make sure they are
installed at the correct version.

We will start by running the following commands to create and preview the
react application.

`npx create-react-app my-app`

`cd my-app`

`npm start`

Go to <http://localhost:3000> in your browser and you will see the default
create-react-app application.

[ ![1
localhost](../../static/958bd7f290b75f722a1c217a5a99ef1a/d9199/1-localhost.png)
](../../static/958bd7f290b75f722a1c217a5a99ef1a/fba00/1-localhost.png)

Now, it’s time to develop the app if you wish to do so, or simply use the
default application. For this tutorial, I made some slight modifications to
the default react app.

[
![2createreactapp](../../static/f3f9e698d7bccd3b78c8630a57bc19a0/d9199/2createreactapp.png)
](../../static/f3f9e698d7bccd3b78c8630a57bc19a0/36eca/2createreactapp.png)

Finally, we need to make a slight modification to the package.json file by
adding the field `homepage: '.'`.

    
    
    {
      "name": "my-app",
      "homepage": ".",
      "version": "0.1.0",
      "private": true,
      "dependencies": {
        "@testing-library/jest-dom": "^4.2.4",
        "@testing-library/react": "^9.3.2",
        "@testing-library/user-event": "^7.1.2",
        "react": "^16.13.0",
        "react-dom": "^16.13.0",
        "react-scripts": "3.4.0"
      },
      "scripts": {
        "start": "react-scripts start",
        "build": "react-scripts build",
        "test": "react-scripts test",
        "eject": "react-scripts eject"
      },
      "eslintConfig": {
        "extends": "react-app"
      },
      "browserslist": {
        "production": [
          ">0.2%",
          "not dead",
          "not op_mini all"
        ],
        "development": [
          "last 1 chrome version",
          "last 1 firefox version",
          "last 1 safari version"
        ]
      }
    }

This will make it so the page will also work on IPFS gateways whose URLs are
in the format `/ipfs/HASH`

Fleek will grab the application from your GitHub repo, so the next thing to do
is to create a GitHub repository with our app in it. This is the repo for the
app above: <https://github.com/SamueleA/create-react-app-ipfs-deploy>Feel free
to fork it. Let’s deploy it now!

### Step 2: Deploying the App Through Fleek

Upon first signing up on Fleek, we are asked to add a new site.

[ ![3 add site](../../static/6f10fe25639ab703c85ffc979e23c453/d9199/3-add-
site.png) ](../../static/6f10fe25639ab703c85ffc979e23c453/07a9c/3-add-
site.png)

Next, we input additional information such as the repo branch, the build
commands, and the build directory. Luckily for us, the default values will
work perfectly so there is no need to change anything. Clicking the “Deploy
Site” button at the bottom will commence the deployment.

Note: The default docker image is `fleek/create-react-app` which runs the
latest node.js version (13 as of this writing). If you have an app requiring
another version, you can specify it in the docker tag. EG: For node 10,
`fleek/create-react-app:node-10`

[
![4reactapp](../../static/087171134c9a152682b6217c9ce4aeb5/f1d1f/4reactapp.png)
](../../static/087171134c9a152682b6217c9ce4aeb5/f1d1f/4reactapp.png)

The deployment is in progress! In a few minutes, we’ll have access to our
deployed app. The deploy log at the bottom of the page tracks the progress of
the deployment.

[
![5reactapp](../../static/58a6cdb35116adcf9bdf6dd246e4c7c8/d9199/5reactapp.png)
](../../static/58a6cdb35116adcf9bdf6dd246e4c7c8/985a9/5reactapp.png)

Success! The deployment worked and the yellow indicator at the top turned blue
and a clickable URL ending in .tmnl.co appeared. This URL is provided by Fleek
and it points to the IPFS deployment.

[ ![6 og success](../../static/4479e4e681bba39dfab8be1d6e2411dd/d9199/6-og-
success.png) ](../../static/4479e4e681bba39dfab8be1d6e2411dd/7e881/6-og-
success.png)

Here is the link to see the result: <https://polished-hat-0578.on.fleek.co/>
You can also click on the “Verify on IPFS” link which will lead you to an IPFS
gateway using the IPFS hash, where the app can be admired in all its
distributed, uncensorable glory.

### **Additional Considerations Concerning Routing**

The app we’ve creating is very simple since it does not contain any routes. In
most serious applications, however, you will want to organize your app into
routes.

One problem that will occur is that the routes will work properly when
accessing the site through the main domain, but will not work when accessing
it through an IPFS gateway with the hash in the path such
as`https://ipfs.io/ipfs/HASH`.

This is due to fact that the gateway is formatted with the hash in a path in
the URL which causes the gateway to think the user is looking for a file while
in reality the user is trying to access the app from a particular route. The
problem is explained in more details
[here](https://youtu.be/EOca15VdP-8?t=155).

The solution we recommend is to use hash routing instead. Urls will then
render in the following format: `https://ifps.io/ipfs/HASH/#/YOUR_ROUTE` and
the problem will be fixed.

Creating the default react app and deploying it to IPFS takes less than 10
minutes, so I invite you to create and deploy your application by signing up
for Fleek.

**Documentation**

[**Create-React-App**](https://reactjs.org/docs/create-a-new-react-app.html)

  * Join our [Community Chat](https://slack.fleek.co/)
  * Follow us on [Twitter](https://twitter.com/FleekHQ)
  * Check out our [Tech Docs](https://docs.fleek.co/)
  * Contact us at support@fleek.co

Published 10 Mar 2020

  * [Tutorial](../../tag/tutorial/)
  * [Guide](../../tag/guide/)

Fleek is all you need to build websites and apps on the new Open Web:
permissionless, trustless, censorship resistant, and free of centralized
gatekeepers. Welcome to the new internet.[](https://www.twitter.com/FleekHQ)

