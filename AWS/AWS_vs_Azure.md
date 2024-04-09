# What are the differences between AWS & Azure?

1. **Naming Conventions** : in AWS an 'instance' is the term for 'virtual machine', in AWS we would 'launch' or 'terminate' one and in Azure we would simply 'create' or 'stop'.
2. **IP Address assignment**: Azure by default offers static IP's whereas AWS doesn't.
3. **Creating Images** : Azure you have to run some commands ('waagent') first before you can capture an image whereas Azure you can just create an image straight away
4. **Resource Groups**: Azure has a requirement for all resources to belong to a resource group whereas AWS has this as an available option to help organise but it's not mandatory.
5. **Virtual Network**: Azure needs you to create a VNet or select an existing one with each vm creation, AWS gives you a default.
6. **Auto Scaling**: The availability zones are associated with an individual subnet in AWS unlike in Azure, we also need a launch template in AWS to specify the details on instances
7. **Monitoring of VMs**: We have to turn on 'detailed monitoring' in Azure to monitor by 1 min intervals to match Azure's default because the default on Azure is 5 minutes. Detailed monitoring costs more which is important to note.