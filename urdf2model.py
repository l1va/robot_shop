import os
import sys
import xml.etree.ElementTree as ET
import re


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

    def validSdfFile(self, root: ET.Element):
        mesh = root.findall('mesh')

        if len(mesh) == 0:
            return False

        return True

    def createModelSdf(self) -> None:
        path_sdf = self.path + "/model.sdf"
        name = os.path.basename(self.path)

        os.system(f"gz sdf -p {self.urdf} > {path_sdf}")

        tree = ET.parse(path_sdf)
        root = tree.getroot()

        valid = self.validSdfFile(root)

        if not valid:
            print('Your files is corrupted')
            return

        for mesh in root.iter('mesh'):
            uri = mesh.find('uri')

            if uri is None or uri.text.startswith("model://") or uri.text.startswith("file://"):
                continue

            res = uri.text

            res = res.replace('./', '')
            res = res.replace('obj', 'dae', obj2dae)

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
        obj2dae = sys.argv[2] == '--obj-to-dae'

    trans = UrdfToSdf(sys.argv[1], obj2dae)
    trans.render()
