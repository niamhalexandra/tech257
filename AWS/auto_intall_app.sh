#!/bin/bash

#Update and upgrade
sudo apt-get update -y
sudo DEBIAN_FRONTEND=noninteractive apt-get upgrade -y

#Install nginx
sudo apt-get install nginx -y
sudo sed -i "s|try_files .*;|proxy_pass http://127.0.0.1:3000;|g" /etc/nginx/sites-available/default
sudo systemctl restart nginx
sudo systemctl enable nginx

#Install node.js
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash - && sudo apt-get install -y nodejs

#Clone repo 
git clone https://github.com/niamhalexandra/tech257-sparta-app2.git

#Navigate to app directory
cd tech257-sparta-app2/app

#Install npm
npm install

#Install pm2
sudo npm install pm2@latest -g

#Stop pm2
pm2 stop app

#Run app with pm2
pm2 start app.js