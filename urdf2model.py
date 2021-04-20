import os
import sys


def urdf2model(urdf, obj2dae=False):
    # example urdf = "manipulators/iiwa14/iiwa14_model.urdf"
    pth = os.path.dirname(urdf)
    model_name = os.path.basename(pth)  # iiwa14 like directory!
    conf_path = pth + "/model.config"
    sdf_path = pth + "/model.sdf"
    # generate config
    conf = """<?xml version="1.0"?>
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
    conf = conf.replace("{name}", model_name)
    conf_file = open(conf_path, "w")
    conf_file.write(conf)

    # generate sdf from urdf
    os.system("gz sdf -p " + urdf + " > " + sdf_path)

    import xml.etree.ElementTree as ET
    # fix all meshes uri - add model://robot to path:
    tree = ET.parse(sdf_path)
    root = tree.getroot()  # sdf
    for m in root.iter("mesh"):
        uri = m.find("uri")
        if uri is None or uri.text.startswith("model://") or uri.text.startswith("file://"):
            pass
        else:
            res = uri.text
            if res.startswith("./"):
                res = res[2:]
            if res.endswith("obj") and obj2dae:  # dirty hack
                res = res[:-3] + "dae"
            uri.text = "model://" + model_name + "/" + res

    res = ET.tostring(root)
    resfile = open(sdf_path, "wb")
    resfile.write(res)
    print("done")


if __name__ == "__main__":
    obj2dae = False
    if len(sys.argv) > 2:
        obj2dae = sys.argv[2] == 'True'
    urdf2model(sys.argv[1], obj2dae)

# examples:
# urdf2model("walking/atlas5/atlas_v5.urdf")
# urdf2model("manipulators/iiwa14/iiwa14.urdf")
