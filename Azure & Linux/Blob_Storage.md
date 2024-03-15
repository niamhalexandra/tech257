# Blob Storage

### What is Blob storage?

_Binary _Large_ _Object_ _Storage_

* Stores unstructured (unorganised) data in blob containers. 


create a script ./'use-blob.sh' for the name

To allow public access to blobs in storage account and in the blob container
add a delay that's long enough using sleep command for approx 15 secs


#Command for creating storage account
az storage account create --name tech257niamhstorage --resource-group tech257 --location uksouth --sku Standard_LRS

#List storage accounts in blob container: 
az storage account list --resource-group tech257 (not v user friendly)

az storage account list --resource-group tech257 --query "[].{Name:name, Location:location, Kind:kind}" --output table (better visual of it, easier to understand)

#Create a container:
az storage container create \
    --account-name tech257niamhstorage \
    --name testcontainer

#OR

az storage container create --account-name tech257niamhstorage --name testcontainer

#The above will create a container but it will give you the recommendation to use 'auth mode' login. In order to follow this recommendation and not recieve a warning code, execute the create from below:

#Delete with recommendation:
az storage container delete \
    --account-name tech257niamhstorage \
    --name testcontainer \
    --auth-mode login

#Create with the recommendation
    az storage container create \
    --account-name tech257niamhstorage \
    --name testcontainer \
    --auth-mode login

#List containers:
az storage container list --account-name tech257niamhstorage --auth-mode login

#OR
#present in table with this alternative:

az storage container list \
    --account-name tech257niamhstorage \
    --output table \
    --auth-mode login

#To upload the blob storage

#Upload blob storage 
az storage blob upload \
    --account-name tech257niamhstorage \
    --container-name testcontainer \
    --name newname.txt \
    --file test.txt \
    --auth-mode login

#Check blob storage in list
az storage container list \
    --account-name tech257niamhstorage \
    --container-name testcontainer \
    --output table \
    --auth-mode login

#Delete the storage account:
az storage account delete -n tech257niamhstorage -g tech257 (might need to add -y to prevent need for user interaction for this in script)

sed command to change the source image tag in the index.ejs with the url of the blob in the container on azure portal

### Full 'history' of commands used:
   1.  curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
   2.  az --version
   3.  az login
   4.  az storage account create --name tech257niamhstorage --resource-group tech257 --location uksouth --sku Standard_LRS
   5.  az storage account list --resource-group tech257
   6.  az storage account list --resource-group tech257 --query "[].{Name:name, Location:location, Kind:kind}" --output table
   7.  az storage container create     --account-name tech25niamhstorage     --name testcontainer
   8.  az storage container create --account-name tech25niamhstorage --name testcontainer
   9.  az storage container create --account-name tech257niamhstorage --name testcontainer
   10. az storage container delete     --account-name tech257niamhstorage     --name testcontainer     --auth-mode login
   11.  az storage container create     --account-name tech257niamhstorage     --name testcontainer     --auth-mode login
   12.  az storage container list --account-name tech257niamhstorage --auth-mode login
   13.  az storage container list     --account-name tech257niamhstorage     --output table     --auth-mode login
   14.  nano test.txt
   15.  cat test.txt
   16.  az storage blob upload     --account-name tech257niamhstorage     --container-name test container     --name newname.txt     --file test.txt     --auth-mode login
   17.  az storage blob upload     --account-name tech257niamhstorage     --container-name testcontainer     --name newname.txt     --file test.txt     --auth-mode login
   18.  az storage container list     --account-name tech257niamhstorage     --container-name testcontainer     --output table     --auth-mode login


#Installing Apache:
sudo apt-get install apache2-utils

#Test installation
ab --version

#test load 1
ab -n 1000 -c 100 http://172.166.175.159/

#test load 2 (faster speed)
ab -n 10000 -c 200 http://172.166.175.159/

ab -n 10000 -c 200 http://172.166.175.159/

#Using this ab command can be used to trigger your alert