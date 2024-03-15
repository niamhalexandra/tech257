# Setting up alerts in Azure Monitor

## What is worst to best in terms of monitoring and responding to load/traffic - diagram:

![alt text](<Screenshot 2024-03-14 at 18.04.48.png>)

## How do we set up a dashboard? 
1. Navigate to your chosen VM
2. Click the tab that says 'Monitoring'
3. You will see some graphs with metrics visible, where the pin symbol is, click that and follow the steps provided to create a dashboard and pin it to it.
4. From there when viewing the dashboard you can customise the view and add/remove from it
5. You can make dashboards both public or private depending on requirements


## How to set up a CPU usage alert 
1. Type in alerts in the search bar
2. Click on the 'create+' button and begin by creating an action group.
3. Here you can provide a name and choose the preferred method for an alert to come through on. In this case I selected email and input the email address I wanted the notification sent to.
4. Once this is set up, you need to then add an alert rule by clicking the 'create+' button again and selecting alert rule
5. Once in the settings page you can configure the type of rule you want to set up. In this case it was CPU usage. 
6. I set it to trigger an alert when CPU usage was > 3% 
7. I then set the 'Aggregation type' to 'Average'
8. I selected 'check every' 1 minute and 'lookback period' 1 minute
9. Making sure this rule was in my specific action group
10. When this was done, to test it I ran the 'ab' command in the terminal and received the below alert to prove it had worked.




## Email alert screenshot:

![alt text](<Screenshot 2024-03-14 at 15.11.57.png>)