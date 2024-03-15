#!/bin/bash

# Update and upgrade
sudo apt-get update -y
sudo apt-get upgrade -y

# Install Nginx
sudo apt-get install nginx -y
sudo sed -i 's|try_files \$uri \$uri/ =404|proxy_pass http://localhost:3000/;|' /etc/nginx/sites-available/default  
sudo systemctl restart nginx

# sudo systemctl enable nginx

# Install Node.js
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash - &&\ 
sudo apt-get install -y nodejs

# Clone repositorygit
git clone https://github.com/niamhalexandra/tech257-sparta-app2.git

# Navigate to app directory
cd tech257-sparta-app2/app/

# Install npm
npm install

# Install pm2
sudo npm install pm2@latest -g

# Stop pm2 
pm2 stop app

# Run app with PM2
pm2 start app.js



#!/bin/bash

# Update and upgrade
sudo apt-get update -y
sudo DEBIAN_FRONTEND=noninteractive apt-get upgrade -y

# Install Nginx
sudo apt-get install nginx -y
sudo sed -i 's|try_files \$uri \$uri/ =404|proxy_pass http://localhost:3000/;|' /etc/nginx/sites-available/default 
sudo systemctl restart nginx
sudo systemctl enable nginx

# Install Node.js
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash - && sudo apt-get install -y nodejs

# Clone repositorygit
git clone https://github.com/niamhalexandra/tech257-sparta-app2.git

# Navigate to app directory
cd tech257-sparta-app2/app

# Install npm
npm install

# Install pm2
sudo npm install pm2@latest -g

# Stop pm2 
pm2 stop app

# Run app with PM2
pm2 start app.js

# Final Script

#Update and upgrade
sudo apt-get update -y
sudo apt-get upgrade -y

#Install nginx
sudo apt-get install nginx -y
sudo sed -i 's|try_files \$uri \$uri/ =404|proxy_pass http://localhost3000/|' /etc/nginx/sites-available/default
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


## Blockers encountered:

1. Initially git push to get the test app zip file onto github was being pushed to master by default, after troubleshooting why it was because a README.md was being created with the repo. After deleting the initial repo, creating a new one without a README.md I was able to push onto the main branch
2. When running with reverse proxy, kept getting an error code, the app would run in port 3000 but still not just with the public IP. after 'nano'ing into the etc/nginx/sites-enabled/default there was actually an extra ";" which was causing an error in the syntax and preventing the script running properly, when removed via the sudo command, it then was accessible via the public ip. 
3. When running on a fresh VM the same errors were encountered. It was clear then that there was something in my bash script that was causing the extra ";" to be added into the config file. I then looked for a colon that may be unecessary in my initial bash script and found it within the reverse proxy command. After removing it, saving the script and re-running it worked without errors.

# User Data

