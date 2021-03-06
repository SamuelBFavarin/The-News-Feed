# The News Feed :newspaper:

This is the Amazing News Feed! This project provides a client interface created with React.js and an API created with Python using Flask. 
  
## Client

The client provides a web interface, to read the most recent news about diverse topics, like Business, Tech, Science, Sports, and Politics. Also, you can filter the news by the same topics, end read the entire news on News Page. 
~~[Click here to open the website](https://www.thenewsfeed.site/)~~ and explore.

\* The project on Google Cloud is temporary unavaliable 

![Home Page](https://i.postimg.cc/Kcqcdbz7/site.png)


## Server

The server provides an API to list and create the news. To create news you must have an Authorization Token, generated by  `/auth`endpoint. Follow these commands to use the API.

The URL to access the API is:
` https://feednews-rt6crd7zeq-uc.a.run.app/ ` 

### [POST /auth] Generate Authorization Token

To create and generate news, you must have an Authorization Token, to create this token, you need to use this command, sent your name and your email.

` curl -X POST "https://feednews-rt6crd7zeq-uc.a.run.app/auth/" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"user\": \"samuelfavarin\", \"email\": \"favarin.dev@gmail.com\"}" `

### [GET /news] List Recent News

This endpoint will return the last 12 news. 
`curl -X GET "https://feednews-rt6crd7zeq-uc.a.run.app/news/" -H "accept: application/json" ` 

Also, you can filter the data using this tag parameters:

 - ` tag=tech`
 - ` tag=politics`
 - ` tag=science`
 - ` tag=business`
 - ` tag=sports`

### [POST /news] Create News

With this endpoint, you can create news. You need to send these attributes to create the news:

    {
      "title": "The news title, is required",
      "text": "The news text, is required",
      "tag": "The news tag, is required",
      "photo": "The news photo",
      "author_name": "The news author, is required",
      "author_photo": "The news photo"
    }

Follow a request example

    curl -X POST "https://feednews-rt6crd7zeq-uc.a.run.app/news/" -H "accept: application/json" -H "Authorization: <Your Auth Token>" -H "Content-Type: application/json" -d "{ \"title\": \"US Congress overrides Trump veto for first time\", \"text\": \"The US Congress has overturned President Donald Trump's veto of a defence spending bill, the first time this has happened in his presidency. The Republican-controlled Senate held a rare New Year's Day session to debate the move, which had already been voted for by the House of Representatives.\", \"tag\": \"POLITICS\", \"photo\": \"https://ichef.bbci.co.uk/news/976/cpsprodpb/99C2/production/_116326393_trumpmelaniaepa.jpg\", \"author_name\": \"BBC\"}"

### [POST /webscraping] Generate News 

This endpoint is used by CRON to generate and scraping the most recent news on the https://www.theguardian.com/ website. Also, you can call this API using this command.

    curl -X POST "https://feednews-rt6crd7zeq-uc.a.run.app/webscraping/" -H "accept: application/json" -H "Authorization: <Your Auth Token>"  

## Architecture

The following image represents the technologies used to create and host this project.

![Architecture Schema](https://i.postimg.cc/V6F9Y6Tk/Feed-News-Tech.png)

## Run Locally
To run the client app, go to `./client` and run these commands
 - `npm install`
 - `npm start`

To run the server app, got to `./server` and run these commands

 - `pip  install  -r  requirements.txt`
 - `python main.py db init `
 - `python main.py run`


#### Migrations:

 - ` python main.py db init ` 
 - ` python main.py db stamp head ` 
 - ` python main.py db migrate --message 'your message' ` 
 - ` python main.py db upgrade `

#### Test
` python main.py test `

    
## Deploy

### Server deploy
The project back-end api is hosted on Google Cloud Platform, using the Cloud Run Service. To deploy, you must have installed the `GCLOUD SDK` on your computer.

##### Build the container by DockerFile 
` gcloud builds submit --tag gcr.io/the-news-feed-299619/feednews`

##### Deploy to Google Cloud Run
``` gcloud run deploy --image gcr.io/the-news-feed-299619/feednews --platform managed --add-cloudsql-instances the-news-feed-299619:us-central1:news-feed-db --update-env-vars INSTANCE_CONNECTION_NAME="the-news-feed-299619:us-central1:news-feed-db"```

##### Create a Job in Cloud Scheduler
  ``` gcloud beta scheduler jobs create http PUSH --schedule="0 */1 * * *" --uri="https://feednews-rt6crd7zeq-uc.a.run.app/webscraping/" --description="generate news" --headers="Authorization=<Your Auth Token>" --http-method="POST"```
  
### Client deploy

The front-end is hosted on Google Firebase, using the Firebase Hosting. To deploy, you must have installed the `FIREBASE SDK` on your computer.

` firebase login `
` firebase use the-news-feed`
` firebase deploy`

 

  
