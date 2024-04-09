# WHat is an AMI?

*AMI's are like templates we can use to launch instances/vm's, they have pre-onfigured settings whether that's for certain security groups or user data that installs required dependencies etc, by creating an AMI (image) of these initial instances with our required configurations we can then use that image to launch new instances/vm's further down the line based on that image to save time on going through the process of specifying these same settings/pre-requisites again over and over.*


# Creating an AMI on AWS

1. Navigate to the instance with the User Data required to install all the desired dependancies, then when in the summary, click 'Actions' > 'image and templates' > 'create image'

![alt text](<Screenshot 2024-04-09 at 11.26.11.png>)

# Deleting an AMI:

1. When on the AMI summary we can go to 'Actions' > 'Deregister AMI' here it will give us a warning that we will also need to delete our 'snapshot' of the image.
2. Copy the id of the snapshot (as prompted) and open it in a new tab (this will save you time searching for it later on) 
3. 'Deregister' the image, go to the other tab and 'delete snapshot' 

![alt text](<Screenshot 2024-04-09 at 11.37.18.png>)


