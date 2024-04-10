!#/bin/bash

sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get upgrade -y

# Install MongoDB
sudo apt-get install gnupg curl
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
sudo apt-get update -y 
sudo apt-get install -y mongodb-org=7.0.6 mongodb-org-database=7.0.6 mongodb-org-server=7.0.6 mongodb-mongosh=2.1.5 mongodb-org-mongos=7.0.6 mongodb-org-tools=7.0.6

# Config bind IP
# sudo nano /etc/mongod.conf
sudo sed -i 's@127.0.0.1@0.0.0.0@' /etc/mongod.conf

# Start/Enable MongoDB
sudo systemctl start mongod
sudo systemctl enable mongod

#MOVING TO APP VM to SET DB_HOST

#set up using private IP address
export DB_HOST=mongodb://10.0.3.4:27017/posts

#Get app up and running:
sudo -E npm install
sudo -E npm start

###########################

DB SCRIPT

!#/bin/bash

sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get upgrade -y

# Install MongoDB
sudo apt-get install gnupg curl
curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg \
   --dearmor
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.>
sudo apt-get update -y 
sudo apt-get install -y mongodb-org=7.0.6 mongodb-org-database=7.0.6 mongodb-org-server=7.0.6 mongodb-mongosh=2.1.5 mongodb-org-mongos=7.0.6 mongodb-org-tools=7.0.6

# Config bind IP
# sudo nano /etc/mongod.conf
sudo sed -i 's@127.0.0.1@0.0.0.0@' /etc/mongod.conf

# Start/Enable MongoDB
sudo systemctl start mongod
sudo systemctl enable mongod

#####################

ps aux | grep "pm2"
kill <pm2-process-id> 

#set up using private IP address
export DB_HOST=mongodb://10.0.3.4:27017/posts

# Cd into app folder
cd tech257-sparta-app2/app

#Get app up and running:
sudo -E npm install
sudo -E npm start

# For aws:

#!/bin/bash

#extra line to disable reboot dialog
sudo sed -i "s/#\$nrconf{restart} = 'i';/\$nrconf{restart} = 'a';/g" /etc/needrestart/needrestart.conf

# Update and upgrade
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get upgrade -y

# Install MongoDB
sudo apt-get install -y gnupg curl
curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg --dearmor
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
sudo apt-get update -y
sudo apt-get install -y mongodb-org=7.0.6 mongodb-org-database=7.0.6 mongodb-org-server=7.0.6 mongodb-mongosh=2.1.5 mongodb-org-mongos=7.0.6 mongodb-org-tools=7.0.6

# Configure bind IP
sudo sed -i 's@127.0.0.1@0.0.0.0@' /etc/mongod.conf

# Start/Enable MongoDB
sudo systemctl start mongod
sudo systemctl enable mongod



#####

# On the app create script below:

# Check and kill existing PM2 processes
pm2_pid=$(ps aux | grep "pm2" | grep -v "grep" | awk '{print $2}')
if [ ! -z "$pm2_pid" ]; then
    sudo kill "$pm2_pid"
fi

# Set up database connection using private IP address
export DB_HOST=mongodb://172.31.50.92:27017/posts

# Cd into app folder
cd tech257-sparta-app2/app

# Get app up and running
sudo -E npm install
sudo -E npm start

