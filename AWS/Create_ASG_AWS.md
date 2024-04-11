# Auto-scaling groups in AWS

## Auto Scaling Diagram

![alt text](<Screenshot 2024-04-10 at 09.29.25.png>)

## Benefits of High Availability with ASG's

* Improved Reliability: Auto Scaling Groups distribute workloads across instances, reducing downtime due to hardware failures or maintenance issues - this is because I already have 2 instances as a minimum, if anything went wrong with one I would already have another to continue running.
* Fault Tolerance: If one instance fails, Auto Scaling automatically replaces it with a healthy one, ensuring constant availability of your application so if something went wrong with instance 1 a healthy one would be created automatically to replace the instance that which initially failed.
* Geo-Redundancy: AWS allows you to deploy resources across multiple Availability Zones (AZs) within a region, each with an associated subnet, this improves fault tolerance, disaster recovery and can help improve security. Each of the 3 instances I specified will all have a dedicated subnet and be in a different availability zone, this means that if anything happened, not just to my particular instance but the wider data centre then my app would still run because I'd have the other instances working as they are in different availability zones, located in a completely different data centre.

#### Benefits of Scalability:
* Improved Resource Management: Auto Scaling Groups automatically adjust the number of instances based on demand, allowing you to scale resources up and down or in and out based on certain criteria you choose to set. I'd set up my ASG so that if the CPU reached 50% then a new instance would be created to cope with the demand.
* Cost Optimisation: Auto scaling helps optimise costs, given the above point, this means you are only paying in accoradance with your usage. Whilst the demand is low I just pay for my two instances that I have as a desired/minimum, I'd only pay for that 3rd instance if it was absolutely necessary - when there was high demand.
* Improved Performance: Your application is ready to handle varying levels of traffic without any negative impacts on it's performance. With my two instances and load balancer traffic is redirected to the initial instances evenly rather than all onto one specific instance at a time.
  
# How to create an auto scaling group:


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

