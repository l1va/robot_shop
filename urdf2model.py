
name = "iiwa"
urdf = "manipulators/iiwa14/iiwa14.urdf"
sdfconf = "manipulators/iiwa14/model.config"
sdf = "manipulators/iiwa14/model.sdf"

#generate config
res = """<?xml version="1.0"?>
<model>
  <name>{name}</name>
  <version>1.0</version>
  <sdf version="1.6">model.sdf</sdf>

  <author>
    <name>Mike Generator</name>
    <email>lev_matematik@tut.by</email>
  </author>
  <description>
    A generated from urdf {name} model.
  </description>
</model>
"""
res = res.replace("{name}", name)
resfile = open(sdfconf, "w")
resfile.write(res)

#generate sdf from urdf
import os
os.system("gz sdf -p "+urdf+" > "+ sdf)

import xml.etree.ElementTree as ET


#fix all meshes uri - add model://robot to path:
tree = ET.parse(sdf)
root = tree.getroot() # sdf
for m in root.iter("mesh"):
    uri = m.find("uri")
    if uri is None or uri.text.startswith("model://"):
        pass
    else:
        uri.text = "model://iiwa14/"+uri.text

res = ET.tostring(root)
resfile = open(sdf, "wb")
resfile.write(res)
