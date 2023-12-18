# flask_e2e_project

# Flask app 1 with oauth



https://github.com/malh718/flask_e2e_project/assets/102617334/6f72a7f5-3e97-4e19-9d04-4ffefba048a9




# Flask app 2 without oauth

# web service requirements
## Create a product using a version control system (Github)
<img width="927" alt="Screen Shot 2023-12-14 at 9 49 01 PM" src="https://github.com/malh718/flask_e2e_project/assets/102617334/cb698893-2225-4592-bc3f-cd33decc86e7">

In the screenshot above, I cloned the flask_e2e_project and I did a git add ., git commit -m, and a git push to push all the changes to my github.

## Create a product that uses envirornment variables (.env)

<img width="892" alt="Screen Shot 2023-12-14 at 9 51 23 PM" src="https://github.com/malh718/flask_e2e_project/assets/102617334/e8a1ef69-14e0-4f09-9ab0-9d5a38cb8351">


^ example of my gitignore file 

My .env variables incluse GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET
GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')


## tailwind
1. My app has many styles and the log in page opens to a blue background and the dashboard page opens to a green background. I was able to change this and more using tailwind.
   Did this using code like 
  <footer class="text-center p-4 bg-purple-300 text-white">
    <p>Copyright © 2023 My Flask App</p>
</footer>
</body>
</html>  on corresponding html pages. 

<img width="1352" alt="Screen Shot 2023-12-18 at 10 52 34 AM" src="https://github.com/malh718/flask_e2e_project/assets/102617334/feded152-66b9-47af-9e0e-2406fe8dba59">

<img width="1142" alt="Screen Shot 2023-12-18 at 10 53 02 AM" src="https://github.com/malh718/flask_e2e_project/assets/102617334/3490f220-54d8-4364-89ef-fc31c7110bab">


## Create a product that is containerized (Docker)
1. Set up flask ensure you are in the correct directory
2. build your docker image, I named mine maliha2
3. After this you should see multiple lines of blue code showing what is built and how much time it takes
4. input docker images to see information
5. input code docker run -p 8005:5000 maliha2 . This will get your app up and running
6. It succesfully ran and is accessible locally and change my port to 8005.
   It should open to the log in page.
7. The container is adf7adfbf5a4b7a488168231e1fdc3725ffb92a6414ee0270350a7a18912fc7b
8. Docker ps  lets you view the containers. Here, it shows the container ID, image name, status, ports as well as a name suspicious_shockley.
9. I then pressed docker stop with the id which will return an empty table back which means it stopped succesfully
<img width="1397" alt="Screen Shot 2023-12-18 at 10 24 08 AM" src="https://github.com/malh718/flask_e2e_project/assets/102617334/7673ab3d-2279-4623-b360-f08a13957771">

## Google API- Maps Embed API
In my Cancer Patient Table, I included a simple map image of Long Island beause the data displayed is cancer patients solely from Long Island.

<img width="579" alt="Screen Shot 2023-12-18 at 12 05 39 PM" src="https://github.com/malh718/flask_e2e_project/assets/102617334/75ae8abb-2c9b-4628-a20f-b0650678c5f9">

<img width="645" alt="Screen Shot 2023-12-18 at 11 58 38 AM" src="https://github.com/malh718/flask_e2e_project/assets/102617334/fcb31eab-f1fa-4d6f-9137-4cd39dfbe651">

It was straightforward and I had to make sure my api key was private and in my .env. The code was     <iframe width="600" height="450" style="border:0" loading="lazy" allowfullscreen src="https://www.google.com/maps/embed/v1/place?q=place_id:ChIJy6Xu4VRE6IkRGA2UhmH59x0&key=AIzaSyCI4TXTYXT5GOHEZnwj1lnOniYj3iywvQs"></iframe>    


## Flask app
This is my flask app. 
<img width="1257" alt="Screen Shot 2023-12-18 at 10 55 45 AM" src="https://github.com/malh718/flask_e2e_project/assets/102617334/8e7388ed-bc20-40b4-9917-aed35777d704">


## Oauth
   1. I was able to succesfully use Google OAuth, so that when you first open up Flask app 1, it brings you into the log in page.
   2. Once you have entered your Google Log In information, it brings you to the dashboard. The dashboard is stylized and shows your user information. Furthermore clicking on the button that says "CLICK HERE TO LOOK AT PATIENT DATA" will direct you to the map API and cancer patient data table.
   3. On this page we have our Maps Embed API

## SQL Alchemy 
   1. In order for me to get SQLalchemy to work and display fake cancer patient information for me, I had to make another app without the OAuth
   2. At this point, I have spent too much time developing and making sure the Google OAuth is functioning properly so I made another app to display my fake information
   3.  While this version does not have the Google Oauth, I was able to create the a table and connect it to the flask app
   4.  I am aware of how to use SQLALchemy, but for some reason no matter how much I tried it would not work with Oauth.
## Sentry.io
   1. I created an account using Sentry.io and connected with my github
   2. From here I was able to create a new flask project and I set up alerts.
   3. I then copied and pasted this information into my app.py file and ran it

   sentry_sdk.init(
    dsn="https://48cd49181c3a276fcafe4ec7563843e6@o4506418102927360.ingest.sentry.io/4506418158043136",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)
   5.   4. /error at the end of the url resulted in a screen that stated " Exception: Something went wrong: division by zero"
   6. This subsequently sent a message to Sentry.io and I received an alert

<img width="1272" alt="Screen Shot 2023-12-18 at 1 30 43 PM" src="https://github.com/malh718/flask_e2e_project/assets/102617334/f6f9ce7b-fbc9-4b3d-a079-0f04d506feb9">