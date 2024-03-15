# Virtual Machine Scale Sets

## Diagram for what they include and break down into:
![alt text](<Screenshot 2024-03-15 at 16.20.54.png>)


## How do we create a scale set? 
1. Navigate to 'Virtual Machine Scale Sets' via the search bar on the Azure portal.
2. Click 'Create+' 
3. Set up the scale set in almost the same way you set up a VM. Fill in the basics such as'Resource group', 'create a name etc'. 
4. This time we want to select the amount of availability zones we want for high availability (in this case zones 1,2 &3)
5. Set the 'Orchestration' mode to 'Uniform'
6. Select the image (this time the one containing user data to run the app)
7. Select the authentication method (for us SSH)
8. Then navigate to 'Disks' select the 'Standard SSD' for 'OS Disk Type'
9. Go to 'Networking' and select the Vnet you want to use (pre-created one for app)
10. Ensure the required inbound ports (http & SSH) are allowed.
11. Choose 'Azure Load Balancer' as the Load balancing option.
12. Now in the 'Scaling' tab, fill in the 'initial instance count' and set that to how many VM's you want initially running.
13. Then select 'Custom' as the scaling policy, configure the minimum and maximum instances you desire. (In our case, 1 min and 3 max)
14. Select the CPU threshold you want to trigger the scale out (75% for us)
15. Select the time duration you want for it to check back and the number of instances you want it to increase by.
16. Go to health and enable the 'application health monitoring'. 
17. Go to 'advanced' input the user data required to run the app immediately from here and then create. 


![alt text](<Screenshot 2024-03-15 at 16.01.39.png>)

![alt text](<Screenshot 2024-03-15 at 16.01.32.png>)

### How do we know it's worked?
1. Navigate to the scale set resource you have just created, there you should be able to copy the 'public IP' and when pasted in the browser your app should be running. 
2. You can also click on 'instances' in the left navigation panel and see if your status is 'running' and also if they are 'healthy'.
   

# I stopped my Scale sets and now my app isn't running?

* It's important to remember that user data is only ran when an instance is first intialised/created and not repeatedly every time it is switched on. This means that if the vms from the scale set are stopped then you will have to get the app running again when you restart them.
* Below is how to do this.

### Reimage

* By navigating to your scale set, in the top section near the options to 'delete', 'restart' and 'stop' your machine there is the option to 'reimage' this will create the virtual machines again from scratch with all of the same prior configurations, when you do this it means the user data is ran again and your app should be working once the vm's are back up and running.

### What is a load balancer?
* Load balancers distribute incoming network traffic across multiple resources to improve availability and performance.
  
### What does a load balancer do?
* They improve scalability by spreading traffic across multiple servers meaning you can just scale out based on workload and app demand
* Availability is increased because of the redundancy but also we can visualise health status'
  
### How to manage Instances:
* You can manage instances by clicking the 'instances' tab on the left hand panel when on the overview of your scale set.
  
### Create an unhealthy instance (for testing)
1. You can stop and re-start your instances

### How to SSH into your instance
1. Select the instance you want to SSH into and copy the IP address, click connect and choose SSH.
2. Select the SSH key you want to use, copy tht key as if you were to SSH normally but instead change the IP address to that specific instances.
3. Use the terminal to SSH into the instance.

### Steps on how to delete VM scale sets
1. In orer to keep track of the components you need to delete (Load balancer, NSG, IP address, and the scale set itself) open up each specific component on different tabs.
2. This is because the scale set needs deleting first so it's easier to keep track of what else needs deleting this way
3. Delete each component in this order... Scale set, Load balancer, IP and then the NSG




ssh -i ~/.ssh/tech257-niamh-az-key -p 50000 adminuser@4.159.36.215

ssh -i ~/.ssh/tech257-niamh-az-key -p 50000 adminuser@4.159.36.215