# Azure Cloud 

### Azure Virtual machines

Azure Virtual machines are comprised as the below diagram:

![c.jpg](..%2F..%2F..%2FDownloads%2Fc.jpg)

* Some names for certain compositions might be referred to by another name in other cloud providers 
* Virtual Machines are accessed via the Azure Portal
* Costings vary, there are free options available
* TCO and Microsofts pricing calculator will assist in predicting costs of on-prem vs cloud options based on business needs to help ensure business' are making the right decision.

## Creating a Vnet in Azure

1. Select Vnet
2. Create
3. Select relevant resource group and complete other relevant details
4. Tags > Include any tags you want for identification

## Create an SSH key for Azure:

1. Open your GitBash terminal, change directory to your .ssh file using "cd ~/.ssh"
2. Use the 'ls' command to list what you have in that file
3. Generate a new SSH key using the command "ssh-keygen -t rsa -b 4096 -C "your_email@example.com""
4. Follow the prompt to create a name for it to be saved as (e.g niamh-azure-key)
4. You can then do an 'ls' to check it's been generated
5. Then perform 'cat (keyname.pub) to reveal the public key 
6. Copy the public key from 'ssh-rsa' to the end of your email address.
7. Then in the Azure portal, navigate to SSH Keys, create new, follow the steps in regards to resource group etc.
8. Change the default selection of 'generate new key' to 'you existing' where it'll prompt you to paste your public key.
9. Then click create
10. Check in your SSH Keys to see that it has been successfully created

### How to create a Virtual Machine: 

1. First navigate to Virtual Machines either via the home screen where it says "Virtual Machines" or via the search bar.
2. When on the Virtual Machines page select "Create" and select "Azure Virtual Machine"
3. You will arrive on the "Basics" section of the creation page. Here you will select the Subscription you're wanting to use (in our case, default Azure Training), then within that select the resource group. In this instance "tech257"
4. You'll then be prompted to enter a Virtual Machine Name, make sure this is clear for identification... we are using "niamh-first-vm"
5. Then select the region you want this Virtual Machine to reside in. In this case "(Europe) UK South"
6. It will then give you the option to select Availability options and Zones, with this being a test we don't need that level of redundancy so we select "No infrastructure redundancy required"
7. We are then prompted to choose our security type, we select "Standard" as right now for this VM we only need the basic level of security
8. We then have to choose an "Image" which is essentially like choosing an OS for the base of the VM. For the purpose of ours we select "Ubuntu Pro 18.04 LTS - x64 Gen2" - This may not be listed in the default list, if it isn't, access it via the "see all images" section by searching for it
9. It will then ask us to choose a size. Right now we only need to use "Standard_B1s - 1 vcpu, 1 GiB memory" as we don't need anything bigger for what we will be doing and therefore don't want to incur unnecessary costs
10. We then reach the Authentication type, we need to select "SSH public key", create a username (advised to use "adminuser")
11. It will say "SSH public key source" and be default will want to generate a new key pair, we need to ensure we use the drop down box to,instead, use our existing key so select "Use existing key stored in Azure"
12. We then use the "Stored Keys" drop down to choose our individual key (Mine being "niamh-az-key" )
13. We then ensure the "Allow selected ports" rule is selected and then using the drop down box below ensure that we have both "HTTP" and "SSH" selected as inbound ports
16. We are then ready to navigate to the next page to set up our "Disks"
15. We then see a drop down box for OS Disk type, it defaults to Premium but we only need to select "Standard SSD".
16. After ensuring the "Delete with VM" box is ticked, we can move on to "Networking" configurations
17. For Virtual Network we then have the option to create a new one but in this scenario we just use the existing one for "tech257"
18. Ensure just basic "Network Security Group" is ticked along with "Delete public IP and NIC when VM is deleted" and we can move on
19. We don't need to make any changes to the default setting for "Management", "Monitoring" or "Advanced" so can move on to "Tags"
20. For identification purposes we want to make sure that in "Tags", the "Name" is set to "Owner" and Value is our first name "(Niamh)"
21. We can then click "Review + Create", after checking the details are correct we can click Create and wait for it to be deployed. 
![Screenshot 2024-03-06 at 16.43.59.png](..%2F..%2F..%2FDesktop%2FScreenshot%202024-03-06%20at%2016.43.59.png)
![Screenshot 2024-03-06 at 16.44.09.png](..%2F..%2F..%2FDesktop%2FScreenshot%202024-03-06%20at%2016.44.09.png)
![Screenshot 2024-03-06 at 16.44.17.png](..%2F..%2F..%2FDesktop%2FScreenshot%202024-03-06%20at%2016.44.17.png)


### How to SSH into a VM
1. Once your VM is up and running, you then want to select "Connect"
2. It will provide you with 2 recommended options, we want to choose "Native SSH"
3. Once you have selected "Native SSH" you will see a section which says "Copy and execute SSH command", in there we need to write the path to our key which begins with "~/.ssh/" and then the key name you wish to use. When you fill that in, you'll see below the SSH to VM box is filled, ready for you to copy to paste into your terminal to access your VM.
4. When you open your terminal paste in the pathway you copied from Azure and press Enter
5. This will give you the automatic response that the "authenticity of host can't be established" this is just because the terminal has no previous record of you accessing this IP and it will as if you are sure you want to continue. To continue you enter "yes"
6. It should then say that the IP is permanently added and will take you into the shell for that VM

### How to delete a Virtual Machine
1. In order to delete a virtual machine you need to be very careful you are deleting the right things. 
2. Firstly navigate to the resource group to locate your VM. 
3. You're going to want to select the VM you wish to delete (checking the box to the left of it to do so), along with also selecting it's other components including: the IP, NSG, Network Interface & Disk
4. Once these are selected you can click delete. It will show a list of what you have selected to delete, when you have ensured this is correct, you can then type "delete" in as prompted and confirm the delete

