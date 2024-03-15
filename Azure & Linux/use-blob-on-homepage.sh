#!/bin/bash

#Create a storage account
az storage account create --name tech257niamhstorage --resource-group tech257 --location uksouth --sku Standard_LRS --allow-blob-public-access true 

#Enable annonymous blob for storage account
az storage account update --name tech257niamhstorage --allow-blob-public-access true 

#Wait for 15 seconds for above command to work
sleep 15

#Create the container 
container_name="catcontainer"
az storage container create --name catcontainer --account-name tech257niamhstorage --public-access blob --auth-mode login

#Download cat pic
curl -o https://thumbs.dreamstime.com/b/cat-hacker-program-develper-laptop-illustration-funny-pet-character-hoodie-playing-computer-generative-ai-art-cat-277323834.jpg

#Rename cat pic
mv https://thumbs.dreamstime.com/b/cat-hacker-program-develper-laptop-illustration-funny-pet-character-hoodie-playing-computer-generative-ai-art-cat-277323834.jpg cat.jpg

#Upload blob
az storage blob upload --account-name tech257niamhstorage --container-name catcontainer --name cat.jpg --file cat.jpg --auth-mode login

#Make blob public
az storage blob update --container-name catcontainer --name cat.jpg --account-name tech257niamhstorage --set "properties.blob.publicAccess=container"

#Change homepage to include cat pic
sed -i 's#<img src=".*">#<img src="https://'tech257niamhstorage'.blob.core.windows.net/'catcontainer'/cat.jpg">#' tech257-sparta-app2/app/views/index.ejs

#Get pm2 to start app
cd tech257-sparta-app2/app
pm2 start app.js