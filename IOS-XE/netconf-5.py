from ncclient import manager
from pprint import pprint
import xmltodict
import xml.dom.minidom
from router_info import router  # used for router_info.py which is in the same directory
# import logging
# logging.basicConfig(level=logging.DEBUG)

# notice that this is an xml file in the same directory
netconf_filter = open("C:/dev/Python/Demos/IOS-XE/netconf-filter.xml").read()

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print('*' * 50)
        print(capability)
    # get the running config on the filtered out interface
    print('Connected')
    interface_netconf = m.get(netconf_filter)
    print('getting running config')
# below, xml is a property of interface_conf

# XMLDOM for formatting output to xml
xmlDom = xml.dom.minidom.parseString(str(interface_netconf))
print(xmlDom.toprettyxml(indent="  "))
print('*' * 25 + 'Break' + '*' * 50)
# XMLTODICT for converting xml output to a python dictionary. interface_netconf var created by calling m.get(netconf_filter)
interface_python = xmltodict.parse(interface_netconf.xml)[
    "rpc-reply"]["data"]
pprint(interface_python)
name = interface_python['interfaces']['interface']['name']['#text']
print(name)

config = interface_python["interfaces"]["interface"]
op_state = interface_python["interfaces-state"]["interface"]

print("Start")
print(f"Name: {config['name']['#text']}")
print(f"Description: {config['description']}")
print(f"Pakcets In {op_state['statistics']['in-unicast-pkts']}")
