# Creating a VM with User data:

1. I created a VM with the same settings and configurations as previous virtual machines created in preparation for the app.
2. This time when it came to the 'advanced' section, I ticked 'enable user data'
3. This opens up a box where I was then able to paste my entire Bash script that I'd previously ran from the terminal after the VM had been created and I'd SSH'd into it.
4. This meant that once the VM was deployed, after I waited a while, I could copy the ip address and it would open in a browser tab without having to SSH into the terminal and run any scripts.

## Creating an image from this VM
1. Navigate to this specific VM and click 'capture' on the top selections pane.
2. This allowed me to name it and choose whether it was just a managed image or would go in the gallery, I chose managed. 

## Creating a VM with little user Data
1. I created a new VM as before this time using the 'Image' of my last virtual machine.
2. After following the previous steps and using the same settings I then went and enabled 'User Data' again.
3. This time I entered just 3 bash commands (as seen below) and when the VM was deployed I could then copy the IP and run the app from the browser.
4. This process was much faster than using just user data but also allowed me to not have to SSH into the terminal to run anything.



# Bash script for little bit of user data:

#!/bin/bash

#Navigate to app directory
cd /tech257-sparta-app2/app

#Stop pm2
pm2 stop app

#Run app with pm2
pm2 start app.js