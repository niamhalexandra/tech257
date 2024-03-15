## Download Azure CLI

#SSH into vm

sudo waagent - deprovision+user

Do you want to proceed? 'y'

do an ls and there's then nothing

### If you're gonna have an app folder don't put it in the home directory because it's going to be deleted in this process - needs to be in adminuser file but Nodejs etc will still be installed

log out with 'exit' to take you back to local computer

"az account show" to tell you who you're logged in as

"az login" to log into your azure account

### Then go into notepad editor to draft below command: This command will stop your VM

'az vm deallocate --resource-group tech257 --name tech257-niamh-sparta-app

### Generalized command - VM has to be generaised in order for settings to be applied when new image is created

'az vm geralize --resource-group tech257 --name tech257-niamh-sparta-app' 

#Then go to your vm, in the details for the VM , then click capture

NO TO share image to azure compute gallery

IMAGE NAME IS IMPORTANT, name of vm -first-image

review and create 

-Use an image to create a new vm

create vm and it will auto fill in the image that's just been created, if not go to see all and gotto my images

Worked successfully in creating the image, couldn't run bash script as was still troubleshooting but hopefully get a chance to do so tomorrow morning.