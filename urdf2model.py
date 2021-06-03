import os
import sys
from typing import Literal
import xml.etree.ElementTree as ET


class UrdfToSdf:

    config_file = """<?xml version="1.0"?>
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

    def __init__(self, urdf_path: str, obj2dae: bool = False) -> None:
        self.urdf = urdf_path
        self.obj2dae = obj2dae
        self.path = os.path.dirname(urdf_path)

    def createModelConfig(self) -> None:
        path_config = self.path + "/model.config"
        name = os.path.basename(self.path)

        self.config_file = self.config_file.replace('{name}', name)

        with open(path_config, "w") as config:
            config.write(self.config_file)

    def createModelSdf(self) -> None:
        path_sdf = self.path + "/model.sdf"
        name = os.path.basename(self.path)

        os.system(f"gz sdf -p {self.urdf} > {path_sdf}")

        tree = ET.parse(path_sdf)
        root = tree.getroot()

        # with open(path_sdf, "r") as sdf:
        #     print(*sdf.readlines(), sep='\n')

        for mesh in root.iter('mesh'):
            uri = mesh.find('uri')

            if uri is None or uri.text.startswith("model://") or uri.text.startswith("file://"):
                continue

            res = uri.text
            print(res)

            if res.startswith("./"):
                res = res[2:]
            if res.endswith("obj") and obj2dae:  # dirty hack
                res = res[:-3] + "dae"

            uri.text = "model://" + name + "/" + res

        res = ET.tostring(root)

        with open(path_sdf, "wb") as sdf:
            sdf.write(res)
            print("done")

    def render(self):
        self.createModelConfig()
        self.createModelSdf()


if __name__ == "__main__":
    obj2dae = False

    if len(sys.argv) > 2:
        obj2dae = sys.argv[2] == 'True'

    trans = UrdfToSdf(sys.argv[1], obj2dae)
    trans.render()

# examples:
# urdf2model("walking/atlas5/atlas_v5.urdf")
# urdf2model("manipulators/iiwa14/iiwa14.urdf")
