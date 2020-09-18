from netmiko import ConnectHandler
from getpass import getpass

username = input('Username: ')
password = getpass()

CSR = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.220',
    'password': password, 
    'username': username
}

net_connect = ConnectHandler(**CSR)

print('-'*79)
print('Saving Config ')
print('-'*79)

output = net_connect.save_config()
print(output)

print('-'*79)
print('Config Saved ')
print('-'*79)



