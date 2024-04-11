# VPC for making Database Instance private

## Diagram of concept:
![alt text](<Screenshot 2024-04-11 at 16.41.54.png>)

1. Create the VPC (virtual private cloud - equivalent to Vnet on Azure)
   ![alt text](<Screenshot 2024-04-11 at 12.01.42.png>)
2. Create two subnets - one public for the app instance and one private for the database instance
   ![alt text](<Screenshot 2024-04-11 at 14.35.59.png>)
   ![alt text](<Screenshot 2024-04-11 at 14.36.05.png>)
3. Make the internet gateway to allow access via internet for end user by navigating to 'Internet gateways' selecting create and giving it a name
4. Associate the internet gateway with the vpc 
5. Create the public route table (private one is created by default)
6. Link route table to public subnet via 'associated subnets' and ensure the 'private-subnet' is in the 'without' section
   ![alt text](<Screenshot 2024-04-11 at 14.40.32.png>)
7. Link route table to internet gateway via routes with the CIDR '0.0.0.0/0' and the destination 'internet gateway'
8. Create DB instance based on an image of a database instance so that it has all the required dependancies and so can be completely private - ensuring you create a new 'security group' specifying port 27017 to allow mongodb and also specify from where with the CIDR block of your public subnet so it can only be accessed via the app vm
   ![alt text](<Screenshot 2024-04-11 at 14.53.04.png>)
9.  Create App instance based on an AMI with the app dependencies installed with the bit of user data to set up the export command (with the private ip of the database instance) 
10. Test by visiting the public IP of the app instance in a browser and accessing the database with /posts
![alt text](<Screenshot 2024-04-11 at 15.03.43.png>)
![alt text](<Screenshot 2024-04-11 at 15.03.55.png>)