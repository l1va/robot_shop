import xml.etree.ElementTree as ET

tree = ET.parse('worlds/default.world')
root = tree.getroot()  # sdf
world = root[0]  # world

incl = ET.SubElement(world, 'include')
uri = ET.SubElement(incl, 'uri')
uri.text = "model://manipulators/iiwa14"

# <pose>0.2 0 0.2 0 0 0</pose>

res = ET.tostring(root)
resfile = open("result.world", "wb")
resfile.write(res)


