# print and separate each item by |
print("server", "device", "network", sep="|")

prefix = 24
print("network mask prefix: ", prefix, sep="/")

Output:
network mask prefix: /24
url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces"
headers = {'Content-Type': 'application/yang-data+json',
           'Accept': 'application/yang-data+json'}

#### TESTING GIT SET UP

response = requests.get(url, auth=(USER, PASS), headers=headers, verify=False)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import json
with open('iosxe_data.json') as json_file:
    data = json.load(json_file)
    for interface in data['ietf-interfaces:interfaces']['interface']:
        print(interface)

from time import sleep
while True:
    try:
        print("Polling.")
        # Poll some resource
        sleep(1)
    except KeyboardInterrupt:
        break

Note: You can use 'Ctrl-C' to break out of infinite loops or hung scripts.

for switch in my_network:
    for interface in switch:
        if interface.is_down() and interface.last_change() > thirty_days:
            interface.shutdown()
            interface.set_description("Interface disabled per Policy")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


import requests

HOST = 'ios-xe-mgmt.cisco.com'
USER = 'developer'
PASS = 'C1sco12345'


url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces"
headers = {'Content-Type': 'application/yang-data+json',
...               'Accept': 'application/yang-data+json'}

response = requests.get(url, auth=(USER, PASS), headers=headers, verify=False)


interfaces = response.json()
interfaces['ietf-interfaces:interfaces']['interface'][0]['name']
'GigabitEthernet1'
interfaces['ietf-interfaces:interfaces']['interface'][0]['ietf-ip:ipv4']['address'][0]['ip']
'10.10.20.48'

