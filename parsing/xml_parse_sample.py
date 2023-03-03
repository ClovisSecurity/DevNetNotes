from lxml import etree as ET

# Get XML File Data
stream = open('sample.xml', 'r')

# Parse data into ElementTree Obj
xml = ET.parse(stream)

# Get the root element from the ElementTree
root = xml.root.getRoot()

# Iterate through child of the root element
for child in root:
    
    # Print Stringified version of the element
    print(ET.tostring(child))
    print("")
    
    # Print the "Id" element of the Element Obj
    print(child.get("Id"))