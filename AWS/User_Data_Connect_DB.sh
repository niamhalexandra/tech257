#!/bin/bash

#Navigate to app directory
cd /tech257-sparta-app2/app

# Set up database connection using private IP address
export DB_HOST=mongodb://10.0.3.76:27017/posts

# Get app up and running
npm install
npm start

#Install pm2
npm install pm2 -g

#Stop pm2
pm2 stop app

#Run app with pm2
pm2 start app.js

