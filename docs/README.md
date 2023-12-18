# flask_e2e_project
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

## Flask app
This is my flask app. 
<img width="1257" alt="Screen Shot 2023-12-18 at 10 55 45 AM" src="https://github.com/malh718/flask_e2e_project/assets/102617334/8e7388ed-bc20-40b4-9917-aed35777d704">

