from collect_world import World
from urdf2model import UrdfToSdf


def example_world():
    world = World("worlds/default.world")
    world.include_model("iiwa14")
    world.include_model("mars_rover", pose=[4, 4, 4, 0, 0, 0])
    world.include_model("atlas5", pose=[1, 1, 1, 0, 0, 0])
    world.include_model("atlas5", pose=[3, 3, 3, 0, 0, 0], name="atlas5_2")
    world.include_model("cheetah", pose=[5, 5, 5, 0, 0, 0])
    world.include_model("a1", pose=[2, 2, 2, 0, 0, 0])
    world.include_model("iiwa14", pose=[2, 0, 0, 0, 0, 0], name="iiwa14_2")

    world.generate("result.world")


def example_urdf2model():
    trans = UrdfToSdf("manipulators/iiwa14/iiwa14.urdf")
    trans.render()


# example_urdf2model()
example_world()
