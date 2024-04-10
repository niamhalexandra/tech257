# Setting up app with HA-SC

1. Create a database instance in the same way as documented for VM on Azure. 
2. SSH in and run bash script for installation of MongoDB (as on Azure)
3. It is important however to add the below command to ensure there is no user input needed when running this on AWS:
   "sudo sed -i "s/#\$nrconf{restart} = 'i';/\$nrconf{restart} = 'a';/g" /etc/needrestart/needrestart.conf"

4. Check that mongoDB is running with command "sudo systemctl status mongod"
5. Modify the launch template to include the User data with the export command to enable connectivity between the database instance and the app. Make sure you are using the private IP as we are wanting the databse to be secure. 
6. Navigate to "Auto scaling groups' and create a new one using the template (and version) you just created. 
7. Set it up with the desired configurations and tags as documented previously.
8. Wait for the instance's to initialize and run.
9. Check via Load Balancer DNS in browser to see if the app is running correctly with /posts

![alt text](<Screenshot 2024-04-10 at 14.29.43.png>)