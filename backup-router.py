from netmiko import ConnectHandler

#First create the device object using a dictionary
CSR = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.220',
    'username': 'roger',
    'password': 'cisco'
}

# Next establish the SSH connection
net_connect = ConnectHandler(**CSR)

#Discover the hostname from the prompt 

hostname = net_connect.send_command('show run | i host')
hostname.split(" ")
hostname,device = hostname.split(" ")
print ("Backing up " + device)

filename = '/home/roger/python-scripts-for-network-engineers/backups/' + device + '.txt'
# to save backup to same folder as script use below line and comment out above line 
# filename = device + '.txt' 

showrun = net_connect.send_command('show run')
showvlan = net_connect.send_command('show vlan')
showver = net_connect.send_command('show ver')
log_file = open(filename, "a")   # in append mode
log_file.write(showrun)
log_file.write("\n")
log_file.write(showvlan)
log_file.write("\n")
log_file.write(showver)
log_file.write("\n")

# Finally close the connection
net_connect.disconnect()
