Requirements to deploy sparta test app

1. manually - working commands, must work without user input
2. automate with Bash Script

### On Azure VM, we will need: 
1. Ubuntu 22.04 LTS - DONE
2. Update & Upgrade (issue with user prompt with upgrade command)
3. install web server - nginx (+ make sure it's enabled)
4. INSTALL right version of node.js version 20. x
5. FIND OUT HOW TO COPY APP FOLDER TO VM 'app' folder with code in - do the git clone after you're logged in
6. 1. npm install
7. 2.npm start OR node app.js
8. *When you install node.js it will auto install node package manager (npm)

cd into folder 



## How to copy app folder to vm

do src first... 

then try pushing to github and then the clone onto vm

install and use 'PM2' to run in the backround

to test your app is running in browser:

public ip address:3000

CTRL+C to exit