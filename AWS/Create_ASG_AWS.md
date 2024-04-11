# Auto-scaling groups in AWS

# Auto Scaling Diagram

![alt text](<Screenshot 2024-04-10 at 09.29.25.png>)

## Benefits of High Availability with ASG's

* Improved Reliability: Auto Scaling Groups distribute workloads across instances, reducing downtime due to hardware failures or maintenance issues
* Fault Tolerance: If one instance fails, Auto Scaling automatically replaces it with a healthy one, ensuring constant availability of your application.
* Geo-Redundancy: AWS allows you to deploy resources across multiple Availability Zones (AZs) within a region, each with an associated subnet, this improves fault tolerance, disaster recovery and can help improve security.

## Benefits of Scalability:
* Improved Resource Management: Auto Scaling Groups automatically adjust the number of instances based on demand, allowing you to scale resources up and down or in and out based on certain criteria you choose to set.
* Cost Optimisation: Auto scaling helps optimise costs, given the above point, this means you are only paying in accoradance with your usage.
* Improved Performance: Your application is ready to handle varying levels of traffic without any negative impacts on it's performance.
  
## How to create an auto scaling group:


1. Navigate to autoscaling groups, click 'create'
2. Give the auto scaling group a name and select the launch template you want to use to configure the instances from
3. Select the availability zones you want to use (in this instance 1 a,b & c)
4. Select 'Attach to a new load balancer' in 'Load balancing' and choose 'Application Loadbalancer'
5. Give that load balancer a name and choose the 'scheme' (internet-facing) for this one
6. Create a target group and add a name
7. We then need to check the box for 'Turn on Elastic Load Balancing health checks'
8. We then want to determine the minimum amount of instances to 2, the maximum to 3 and the desired as 2.
   ![alt text](<Screenshot 2024-04-09 at 16.04.09.png>)
9.  Add a tag to make the group distinguisable and then review and create. 
10. When created, wait a while then you can navigate to the Load balancer, get the DNS name and paste that into your browser to see if the app is running and the autoscale group was set up correctly.

![alt text](<Screenshot 2024-04-09 at 16.02.54.png>)

