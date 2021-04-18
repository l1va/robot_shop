
name = "iiwa"
urdf = "manipulators/iiwa14/iiwa14.urdf"
sdfconf = "manipulators/iiwa14/model.config"
sdf = "manipulators/iiwa14/model.sdf"

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

import os
os.system("gz sdf -p "+urdf+" > "+ sdf)
