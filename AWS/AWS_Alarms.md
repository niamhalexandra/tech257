# Creating Alarms in AWS

1. When on your specific EC2's page, navigate to 'monitoring' along the bottom, click on 'manage detailed monitoring' and select 'enable'
2. Then click on 'add to dashboard' to add this EC2's monitoring to a dashboard (see dashboard documentation for more info)
3. At the dashboard page in the left 'cloudwatch' pane there is a section for alarms, click 'all alarms' and then choose 'create alarm'
4. Choose 'all metrics' set the period of time, and select 'EC2' in the browse section, then choosiong 'Per-instance Metrics' after that.
5. Search for the desired EC2 instance in the list of instances and select the instance needed and the metric you want to measure. 
6. Set the conditions as required, for instance set the CPU usage to a percentage and whether you want it as an average etc across the period you wish to see. 
7. For notification select SNS topic (you can create a new one there) enter the email address you want to be alerted etc. 
8. Give the alarm a name and description and complete.
9. You will get an email to the specified email address, ensure you 'confirm subscription' in this email otherwise you will NOT recieve any alerts even if your condition is met. 
    
    ![alt text](<Screenshot 2024-04-16 at 09.33.37.png>)

10. Your graph's will show spikes with matching conditions that are met in the graphs in dashboard, similar to below:
    ![alt text](<Screenshot 2024-04-16 at 09.33.15.png>)

11. When the condition is met, and the alarm is triggered, you'll get an email alert like below:
    
    ![alt text](<Screenshot 2024-04-16 at 09.31.13.png>)