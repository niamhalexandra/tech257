# Process of Running the app based on an image with SOME user data

###Initial blocker:
 * After successfully getting my script to run via ssh'ing in and adding it as a bash script, I pasted the same script in User Data but could only then run it when manually entering port 3000 with the IP address. 
 * After nano'ing into the etc/nginx/sites-available/default file, and reviewing the 'sed' command line there was no ":" inbetween local host and 3000, after adding this in, the app ran and I didn't have to go to port 3000.
 * I then added the colon to my initial bash script, input it in user data and it worked.

## Creating an image of the VM containing User Data:

1. Went to my virtual machine with the User Data and used 'Capture' to create an image of it. 
2. In the creation, in advanced I added the user data to cd into the app file and start the app, as follows: "cd tech257-sparta-app2/app" and "pm2 start app.js


### Commands used before editing script to remove "/" 

 cd /
    2  ls
    3  cd tech257-sparta-app2
    4  cd app
    5  kill-9 1118
    6  kill -9 1118
    7  pm2 start app.js
    8  pm2 list
    9  cd /
   10  cat /etc/nginx/sites-available/default
   11  nano  /etc/nginx/sites-available/default
   12  systemctl restart nginx