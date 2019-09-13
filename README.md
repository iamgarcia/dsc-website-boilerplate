# DSC Website Boilerplate

# Table of Contents

- [Getting Started](#getting-started)
    - [Installing Python 2.7](#installing-python-2.7)
    - [Installing Google Cloud SDK](#installing-google-cloud-sdk)
    - [Setup App Engine Project](#setup-app-engine-project)
    - [Running a Local Server for Testing](#running-a-local-server-for-testing)
    - [Deploying the Website to the Cloud](#deploying-the-website-to-the-cloud)
- [FAQ](#faq)
- [Authors](#authors)
- [Contributors](#contributors)

# Getting Started

## Installing Python 2.7
Head over to [Python.org](https://www.python.org/downloads/) and download the latest version of Python 2.7. Make sure you add
Python 2.7 to your system's path.

## Installing Google Cloud SDK
Head over to Google's [Cloud SDK for Python 2](https://cloud.google.com/appengine/docs/standard/python/download). Once on
that site, you need to complete steps 2, 3, and 5 of the **Installing Cloud SDK for Python 2**.

## Setup App Engine Project
Clone this repository and cd to it using the command line. Once in the folder, type: 

```
    C:\Projects\dsc-csusm> gcloud init 
```

This will initialize the gcloud project in the folder.
We want to create a new configuration so go ahead and choose **Create a new configuration**.

Next, it's going to ask you to name the project. You can name it whatever you'd like. 
After that, you're going to want to **Log in with a new account**. Go ahead an log in with a
non-school related email. Again, **DO NOT USE YOUR SCHOOL EMAIL**.

After that is done, it'll ask you to pick a cloud project. Since you don't have one, you're
going to select **Create a new project**. For the project ID, go ahead and name it the following: **dsc-your-university-name**.

## Running a Local Server for Testing

Since all that is done, you are now able to work on the project and change the HMTL, CSS, JS, etc. anything to make your website unique. But wait, how can I view my changes? Well, good thing I asked huh. Luckily for us, the Cloud SDK has a built in tool for running a local instance of your project. In order to do that, you need to type:

```
C:\Projects\dsc-csusm> dev_appserver.py app.yaml 
```

Once you run this command, it'll start a local server for your project and you can view your changes in real time. Pretty neat! If you want to stop the server for whatever reason, simply **Ctrl + C**. 

## Deploying the Website to the Cloud

Now that you have finished your website, the next thing you need to do is deploy the project to the cloud. Open the command line within the project folder and type:

```
C:\Projects\dsc-csusm> gcloud app deploy --project [project-id] 
```

The [project-id] would be **dsc-your-university-name**. This command deploys your project to the cloud. Anytime you want to publish your changes, you have to do this command. In order to view your website, simply visit www.dsc-your-university-name.appspot.com. That's it! You have your own website now.

# FAQ

## How can I get a custom domain instead of the .appspot.com?
You can read more about getting a custom domain for your app engine project [here](https://cloud.google.com/appengine/docs/standard/python/mapping-custom-domains).

# Authors
"Alexander Garcia" garci877@cougars.csusm.edu

# Contributors
"Ace Gabriel Figueroa" figue032@cougars.csusm.edu