from ncclient import manager
from router_info import router

# there are dynamic variables set in the ios_config.xml file 
config_template = open(
    "E:/dev/CodeSamples/Python/Networking/IOS-XE/ios_config.xml").read()

# here we are setting the variable values that are defined in ios_config.xml
# interface_name and interface_desc are used word-for-word in ios_config.xml
netconf_config = config_template.format(
    interface_name="GigabitEthernet2", interface_desc="daniyal")

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    device_reply = m.edit_config(netconf_config, target="running") # we are passing an edit_config rpc here against running_config
    print(device_reply)
