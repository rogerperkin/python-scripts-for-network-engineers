## Simple Python Script to connect to Cisco Router using Netmiko 

import netmiko 

connection = netmiko.ConnectHandler (ip='192.168.1.220', device_type='cisco_ios', username='roger', password='cisco')

result = connection.send_command('sh ip int brief')

print(result)



