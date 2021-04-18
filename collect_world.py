# import xml.etree.ElementTree as ET
import lxml.etree as ET


class World:
    def __init__(self, world_path):
        # self.world_path = world_path
        self.tree = ET.parse(world_path)
        self.root = self.tree.getroot()  # sdf tag
        self.world = self.root[0]

    def include_model(self, model, pose=None):
        if pose is None:
            pose = [0, 0, 0, 0, 0, 0]
        incl = ET.SubElement(self.world, 'include')
        uri = ET.SubElement(incl, 'uri')
        uri.text = "model://" + model
        pose_tag = ET.SubElement(incl, 'pose')
        pose_tag.text = " ".join("{0:0.2f}".format(i) for i in pose)

    def generate(self, result_path):
        ET.indent(self.root)
        self.tree.write(result_path)
