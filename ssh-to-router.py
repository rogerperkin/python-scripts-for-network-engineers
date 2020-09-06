# Script to connect to Cisco Router using Netmiko

from netmiko import ConnectHandler

CSR1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.220',
    'username': 'roger',
    'password': 'cisco'
}

net_connect = ConnectHandler(**CSR1)

output = net_connect.send_command('show ip int brief')
print (output)

net_connect.disconnect()
