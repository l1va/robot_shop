from collect_world import World
from urdf2model import urdf2model


def example_world():
    world = World("worlds/default.world")
    world.include_model("iiwa14")
    world.include_model("atlas5", pose=[1, 1, 1, 0, 0, 0])
    world.include_model("iiwa14", pose=[2, 0, 0, 0, 0, 0])
    world.generate("result.world")


def example_urdf2model():
    urdf2model("manipulators/iiwa14/iiwa14.urdf")


# example_urdf2model()
example_world()
