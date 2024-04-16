# Make a change and push to Docker repo

1. Create an account with Docker, with that account make a new repo on the Dockerhub site.
2. Go to terminal and perform:
   ~~~
   docker run -d -p 60:80 niamhalexandra/firstrepo:first
   ~~~
3. Perform 'docker ps' to see the image id for the image you just created
4. Enter the shell in Docker for that image using:
   ~~~
   docker exec -it <image id> sh
   ~~~
5. Perform an update and upgrade using usual bash commands
6. Install sudo and nano with bash commands
7. Then cd into /usr > share > nginx > html 
8. sudo nano into 'index.html' and make a change to the file, save and exit. 
9. Use 'exit' to quit the shell
10. Commit the change with:
    ~~~
    docker commit <container id> <dockerhubusername/reponame:tag>
    ~~~
11. Then push the changes with:
    ~~~
    docker push <dockerhubusername/reponame:tag>
    ~~~

12. Check for it in repo, changes should be available to see in browser running on your specified port and should be available to all that run this command in terminal with docker:
    ~~~ 
    docker run -d -p 60:80 niamhalexandra/firstrepo:first
    ~~~

## My Image in browser:

![alt text](<Screenshot 2024-04-16 at 17.21.23.png>)