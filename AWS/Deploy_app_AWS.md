# Deploying the app via AWS:

### Steps are pretty similar to Azure, but the Azure portal has slightly different names for things and the layout of the portal is different.

#### steps:

1. Create EC2 (Elastic Computing Instance), this is the same as 'creating a virtual machine' in Azure.
2. After choosing an image (in this case Ubuntu 22.04) you can go on to configure the networking settings including port rules to allow Http (80), SSH (22) and Custom (3000)
3. You cna connect with SSH just like we had done in Azure, however we have to navigate to the SSH file in the terminal where our key pair is stored. In order to change permissions to use the key we need to use "