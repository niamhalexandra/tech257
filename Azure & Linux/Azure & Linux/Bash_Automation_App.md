#!/bin/bash

# Update and upgrade
sudo apt-get update -y
sudo apt-get upgrade -y

# Install Nginx
sudo apt-get install nginx -y
sudo systemctl restart nginx
sudo systemctl enable nginx

# Install Node.js
curl -fsSL https://deb.nodesource.com/setup_20.x sudo -E bash 
sudo apt-get install -y nodejs

# Clone repositorygit
git clone https://github.com/niamhalexandra/tech257-sparta-app2.git

# Navigate to app directory
cd tech257-sparta-app-2/app

# Install npm
npm install

# Install pm2
sudo npm install pm2@latest -g

# Run app with PM2
pm2 start app.js

