# How to create image of the Sparta Nodejs app

1. Navigate to the folder containing the app
2. Use 'sudo nano' to create a Dockerfile (no need to create a requirements.txt file for dependencies for nodejs) containing the following:
   
   ~~~
   # Specify node version
   FROM node:20
   
   # Create directory
   WORKDIR /nodejsapp
   
   # Copy the json file
   COPY package.json ./
   
   # Copy the other files needed
   COPY . .
   
   # Install npm
   RUN npm install
   
   # Run the app as a non-root user
   USER node
   
   # Open ports to all
   EXPOSE 3000
   
   # Run the app
   CMD node app.js
   ~~~

3. Use the 'docker build' command to create the image
4. Use the 'docker run' command to ensure it's running
5. Check in browser on port 3000 that the app is there running as it should be 

![alt text](<Screenshot 2024-04-18 at 12.22.45.png>)

6. Tag the image in preparation for the push of the image to Dockerhub
7. Use 'docker push' to push the image to Dockerhub
8. Check it's visible on Dockerhub
   
   ![alt text](<Screenshot 2024-04-18 at 12.26.56.png>)