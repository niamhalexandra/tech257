# Using NVA for making a database private:

1. Create a Virtual Network with 3 subnets, one public for the app VM, one dmz for the NVA vm and then a private one for the database vm.
2. Create a vm for the database using a pre-assigned image with prequisites for the database to work
3. Create an App vm with the export DB_HOST=mongodb://10.0.4.4:27017/posts command to enable the MongoDB in user data
4. Create a NVA vm using a fresh image, no pre-requesites required
5. Cerate a route table, enter a name for it etc. 
6. Add rules to the route table using the destination IP address (in this case the Database's) and the address of the location you want to hop from (the NVA)
7. SSH into the Database vm in the terminal, nano into the config file and uncomment the IP forwarding command that exists there already (there are instructions contained in the file)
8. Create a file containing a script that enables the traffic (see below), execute it and then test through accessing the IP via web browser.
   
![alt text](<Screenshot 2024-03-18 at 14.35.00-1.png>)

![alt text](<Screenshot 2024-03-18 at 16.58.44-1.png>)

## IP Tables Script and command meanings:

#!/bin/bash

#configure the ip tables

echo "Configuring iptables..."

#Allow traffic (traffic within the same machine)
sudo iptables -A INPUT -i lo -j ACCEPT
sudo iptables -A OUTPUT -o lo -j ACCEPT

#Allow packets coming in that are part of established connections and are secure
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

#Allow packets that are part of established connections that are outgoing
sudo iptables -A OUTPUT -m state --state ESTABLISHED -j ACCEPT

#Drop packets that are not part of any established connection
sudo iptables -A INPUT -m state --state INVALID -j DROP

#Allow incoming SSH traffic (from port 22) for new and established connections
sudo iptables -A INPUT -p tcp --dport 22 -m state --state NEW,ESTABLISHED -j ACCEPT
sudo iptables -A OUTPUT -p tcp --sport 22 -m state --state ESTABLISHED -j ACCEPT

#Allow forwarding of TCP traffic from subnet 10.0.2.0/24 to subnet 10.0.4.0/24 on port 27017 (for MongoDB)
sudo iptables -A FORWARD -p tcp -s 10.0.2.0/24 -d 10.0.4.0/24 --destination-port 27017 -m tcp -j ACCEPT

#Allow forwarding of ICMP (ping) traffic from subnet 10.0.2.0/24 to subnet 10.0.4.0/24
sudo iptables -A FORWARD -p icmp -s 10.0.2.0/24 -d 10.0.4.0/24 -m state --state NEW,ESTABLISHED -j ACCEPT

#Set policy to drop all incoming packets
sudo iptables -P INPUT DROP

#Set policy to drop all forwarded packets
sudo iptables -P FORWARD DROP

echo "Done!"
echo ""

#Make iptables rules persistent by installing iptables-persistent package
echo "Make iptables rules persistent..."
sudo DEBIAN_FRONTEND=noninteractive apt install iptables-persistent -y
echo "Done!"
echo ""

## Microsoft's Diagram of 3-subnet Architecture:

![alt text](<Screenshot 2024-03-18 at 17.09.45.png>)

## Own Diagram:

![alt text](<Screenshot 2024-03-18 at 17.27.23.png>)
