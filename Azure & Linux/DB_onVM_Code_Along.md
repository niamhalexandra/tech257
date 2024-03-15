# Code along for /posts working:

1. Have your working app VM ready
2. Create a new VM for the Database, create it using the same fresh image vm - ensure that allowed inbound ports are SSH. Make sure it is connected to same vnet and have the subnet as private. 
3. _Why_ _A_ _Private_ _Subnet?_ : Azure by default allows internal traffic and there for the app VM and the Database VM will be able to talk directly without having to back out and in through a specific port in the public IP.
4. Execute the below, manually in the terminal after SSH'ing into the Database VM:


sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get upgrade -y

### Install MongoDB
sudo apt-get install gnupg curl
curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | \ sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg \   --dearmor
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
sudo apt-get update -y 
sudo apt-get install -y mongodb-org=7.0.6 mongodb-org-database=7.0.6 mongodb-org-server=7.0.6 mongodb-mongosh=2.1.5 mongodb-org-mongos=7.0.6 mongodb-org-tools=7.0.6

#### Config bind IP
sudo nano /etc/mongod.conf
sudo sed -i 's@127.0.0.1@0.0.0.0@' /etc/mongod.conf

### Start/Enable MongoDB
sudo systemctl start mongod
sudo systemctl enable mongod

### Check MongoDB is running
sudo sytemctl status mongod

5. After this we need to SSH into the app VM to set the DB_HOST up 


### set up using private IP address (goes just before :27017)
export DB_HOST=mongodb://10.0.3.5:27017/posts

### Get app up and running:
sudo npm -E install
sudo npm -E start

## Blockers:
* Initially had set up my database vm using a different vnet to the app so they couldn't communicate. Rebuilt a new vm on the same vnet as the app vm and successful. 