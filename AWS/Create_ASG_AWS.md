# How to create an Auto-scaling group

1. Navigate to autoscaling groups, click 'create'
2. Give the auto scaling group a name and select the launch template you want to use to configure the instances from
3. Select the availability zones you want to use (in this instance 1 a,b & c)
4. Select 'Attach to a new load balancer' in 'Load balancing' and choose 'Application Loadbalancer'
5. Give that load balancer a name and choose the 'scheme' (internet-facing) for this one
6. Create a target group and add a name
7. We then need to check the box for 'Turn on Elastic Load Balancing health checks'
8. We then want to determine the minimum amount of instances to 2, the maximum to 3 and the desired as 2.
9. Add a tag to make the group distinguisable and then review and create. 
10. When created, wait a while then you can navigate to the Load balancer, get the DNS name and paste that into your browser to see if the app is running and the autoscale group was set up correctly.

![alt text](<Screenshot 2024-04-09 at 16.02.54.png>)

![alt text](<Screenshot 2024-04-09 at 16.04.09.png>)

# Auto Scaling Diagram

![alt text](<Screenshot 2024-04-10 at 09.29.25.png>)