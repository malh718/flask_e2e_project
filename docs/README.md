# flask_e2e_project

# Flask app 1 with oauth

What it is: Long Island Cancer Patient Dashboard


What it does: 
Log in using your gmail account. You will be directed to the dashboard. The dashboard displays user information. From here you can click on the "CLICK HERE TO LOOK AT PATIENT DATA" button. This will direct you to the page with the cancer patient information which includes Patient ID,Cancer type,	First Name,	Last Name,	Date of Birth,	Part of Long Island, and Gender. Additionally there is a map API embedded on this page with a map of Long Island. From here, if you go back to the dashboard you can click on the  Log Out button which will bring you back to the log in page for gmail. 


https://github.com/malh718/flask_e2e_project/assets/102617334/4fd8cbed-c245-4d2c-9b1c-1a51c05049fe



# Flask app 2 without oauth

What it is:  Cancer Patient Oncology Contact Dashboard 

What it does: What this app does is it displays generated Cancer Patient Oncologist Data. I was able to do this using (from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker), to generate the fake dataset. I had tried getting a variation of this on my Flask app but unfortunatley the Oauth would run and nothing else would show up, which  resulted in me displaying the information in this way.  The table includes first name and last name of the patients, date of first cancer emergence, as well as the number to their oncologist. It shows 100 rows and it is also stylized using tailwind. 

<img width="1319" alt="Screen Shot 2023-12-18 at 4 12 23 PM" src="https://github.com/malh718/flask_e2e_project/assets/102617334/fa77116a-ea66-4856-b5cf-ac158e337dff">



( The reason why I made this additional flask app was because I spent many hours attempting to use SQLAlchemy and having the Oauth. I spent many hours on the Oauth, but when I was done and went to add a table it was not letting me do it. After days of troubleshooting I did not want to lose the progress I had made on the first section, I am aware how to use SQLAlchemy and as you can see in this example, I used it to generate patient data.) 

# Brief Explanations

.env file structure

<img width="515" alt="Screen Shot 2023-12-18 at 4 56 04 PM" src="https://github.com/malh718/flask_e2e_project/assets/102617334/0f88bd71-d867-47f1-abcd-9fbbffdfab3f">

How can they run without Docker locally?

1. Make sure you have all packages you need properly installeed
2. Create the app.py and requirements .txt and all other files
3. Make sure you are in the correct directory
4. execute with python app.py
5. App will run locally on device

How can they run it with Docker locally?
0. Make sure you have Docker installed
1.Create a Dockerfile and ensure that is filled out properly and that the requirements.txt file is also correct
2. Create and run app.py and other files
3. Create an image using docker build (container name)
4.To look at your other docker images, simply input docker images
5. Docker ps will show the container id, image, command, created, status, ports and names
6. After that is done correctly, you should see it saying building with multiple columns of blue lines indicating what is being built and how much time it takes
7. Ensure you are in the right port and you can now enter docker run -p 8000:5000 (imagename). 
8. Once this is deployed,  the app should be up and running and can be accessed locally by ensuring the port to 8000.
9. App is running,returns Flask App
10. To stop docker, input docker stop (container id)

How can you deploy it to the cloud?
GCP
1. Open up a project in your Google Cloud Console
2. To view what projects you currently gave in your GCP you can type gcloud projects list(Name, Project ID and Billing Account will be shown)
3. Next you will type gcloud config set project [project id]
4. Ensure that all files are properly created ( ie .yaml file)
5. Ensure you are in the proper directory or else this will not work
6. Insert code gcloud app deploy
7. This will result in an option that says " Please choose the region where you want your App Engine Located"
8. From here you select a choice, customarily I choose 18 which is us-east1
9. Once that is succesful, It will note Creating App Engine application.... done
10. To disable, go into Google Cloud App Engine Setting and Disable the application 

Azure 
1. Create repo in github and populate with corresponding information
2. ensure that the .html files are all aligned with the app.py and that they are in a templates folder
3. Run app.py 
4. Install Azure CLI with code az
5. log in using the code az login --use-device-code
6. Find subscription ID using az account list-- output tables  and then set your ID using az account set --subscription (actual subsciption id)
7. From here create a resource group and do az webapp up- resource group <nameofgroup> --name <app-name> --runtime<PYTHON:3.9> --sku <B1>
8. Deploy with az webapp up
9. To disable/delete type code az webapp delete --name (nameofwebapp)-- resource- group (nameofresourcegroup)



Technologies I used:

Github- Popular version control platform where you can uploud and share code

TailwindCSS- This is a framework for CSS that allows you to create simple,fast user interfaces. Other examples include Bootstrap

Cloud shell editor- This is an online editor that allows you to create, edit files all in one envirornement

Sentry.io- This application helps to see if there are any issues and errors and reports them  

Flask- Python framwework to create apps 

Python- Programming language used with Flask

GCP- Google Cloud Platform, offers a ton of services and APIS 

Azure- Cloud platform for Azure 

Google Ouath- Authorization and  Authentication for applications using google sign in

SQLalchemy- This is an object relational mapping allowing you to make and manipulate databases 


# web service requirements ( all apply to Flask app 1, except for SQLAlchemy bullet)

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

   Did this using code tailwind flask class code as shown below:


<img width="1352" alt="Screen Shot 2023-12-18 at 10 52 34 AM" src="https://github.com/malh718/flask_e2e_project/assets/102617334/feded152-66b9-47af-9e0e-2406fe8dba59">

<img width="1142" alt="Screen Shot 2023-12-18 at 10 53 02 AM" src="https://github.com/malh718/flask_e2e_project/assets/102617334/3490f220-54d8-4364-89ef-fc31c7110bab">

<img width="589" alt="Screen Shot 2023-12-18 at 4 30 19 PM" src="https://github.com/malh718/flask_e2e_project/assets/102617334/7db760fb-398e-43c3-952a-7ed0588ed349">

<img width="1319" alt="Screen Shot 2023-12-18 at 4 12 23 PM" src="https://github.com/malh718/flask_e2e_project/assets/102617334/ab5b8855-6422-4147-bf91-cc29d5ad3b2a">




## SQL Alchemy 
   1. In order for me to get SQLalchemy to work and display fake cancer patient information for me, I had to make another app without the OAuth
   2. At this point, I have spent too much time developing and making sure the Google OAuth is functioning properly so I made another app to display my fake information
   3.  While this version does not have the Google Oauth, I was able to create the a table and connect it to the flask app
   4.  I am aware of how to use SQLALchemy, but for some reason no matter how much I tried it would not work with Oauth and I wasted too much time on it to not use it.

<img width="1319" alt="Screen Shot 2023-12-18 at 4 12 23 PM" src="https://github.com/malh718/flask_e2e_project/assets/102617334/4f175a87-a4f2-45ac-a225-8e774bd398df">


<img width="1159" alt="Screen Shot 2023-12-18 at 4 26 13 PM" src="https://github.com/malh718/flask_e2e_project/assets/102617334/990232c4-a29f-43cf-a6b8-5c65793538c7">

<img width="1091" alt="Screen Shot 2023-12-18 at 4 26 32 PM" src="https://github.com/malh718/flask_e2e_project/assets/102617334/6dae6213-ca1e-4e08-bf10-bd6b07433158">







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
9. I then pressed docker stop with the id which will return an empty table back


<img width="1397" alt="Screen Shot 2023-12-18 at 10 24 08 AM" src="https://github.com/malh718/flask_e2e_project/assets/102617334/7673ab3d-2279-4623-b360-f08a13957771">


<img width="922" alt="Screen Shot 2023-12-18 at 9 17 59 PM" src="https://github.com/malh718/flask_e2e_project/assets/102617334/00a79259-e3b4-4af2-b79a-76139af99cf0">


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


## Sentry.io
   1. I created an account using Sentry.io and connected with my github
   2. From here I was able to create a new flask project and I set up alerts.
   3. I then copied and pasted this information into my app.py file and ran it

   sentry_sdk.init(
    dsn="https://48cd49181c3a276fcafe4ec7563843e6@o4506418102927360.ingest.sentry.io/4506418158043136",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)







   5. /error at the end of the url resulted in a screen that stated " Exception: Something went wrong: division by zero"
   6. This subsequently sent a message to Sentry.io and I received an alert

<img width="1272" alt="Screen Shot 2023-12-18 at 1 30 43 PM" src="https://github.com/malh718/flask_e2e_project/assets/102617334/f6f9ce7b-fbc9-4b3d-a079-0f04d506feb9">


<img width="1438" alt="Screen Shot 2023-12-18 at 1 34 20 PM" src="https://github.com/malh718/flask_e2e_project/assets/102617334/be4b983f-866c-4f65-a4e0-66aacc7ae143">


In my email, I got this later.

<img width="324" alt="Screen Shot 2023-12-18 at 5 07 15 PM" src="https://github.com/malh718/flask_e2e_project/assets/102617334/9c4f00d7-7d62-40dc-808f-cde165071a48">



## Deployment (GCP)
1. Make sure you are in the correct google shell envirornment.
2. I then listed out my projects
<img width="895" alt="Screen Shot 2023-12-18 at 2 03 20 PM" src="https://github.com/malh718/flask_e2e_project/assets/102617334/7b3eed95-3a19-4aa9-8f9f-4ca669759679">

3. For me, my project name is clean-trees-408504
the line of code was  maliha_718@cloudshell:~/flask_e2e_project$ gcloud config set project clean-trees-408504
                                  
5. From here I made sure my .yaml was up to date and that I was in the correct directory
   
<img width="590" alt="Screen Shot 2023-12-18 at 2 12 42 PM" src="https://github.com/malh718/flask_e2e_project/assets/102617334/627a06c0-db45-4627-bf3e-10f1a10fb6cf">

6. After this you deploy using gcloud app deploy and you are all set!!!


<img width="747" alt="Screen Shot 2023-12-18 at 2 30 08 PM" src="https://github.com/malh718/flask_e2e_project/assets/102617334/2b4e231f-fe58-47ff-a203-bdc3c2695283">

<img width="759" alt="Screen Shot 2023-12-18 at 2 31 21 PM" src="https://github.com/malh718/flask_e2e_project/assets/102617334/7789668c-ae70-4dc8-a4ca-a5c80a470278">

Deployed:


<img width="1321" alt="Screen Shot 2023-12-18 at 2 29 10 PM" src="https://github.com/malh718/flask_e2e_project/assets/102617334/ea3bbfb0-e302-45e6-aacf-1633ca4cd3d3">

7. Make sure that you disable the application after the fact, by going into your app engine and selecting the disable application button as shown below
   
   
<img width="417" alt="Screen Shot 2023-12-18 at 2 33 59 PM" src="https://github.com/malh718/flask_e2e_project/assets/102617334/d5555180-5afd-4ed4-9e67-f97502ecb7e2">
