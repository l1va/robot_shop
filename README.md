# robot_shop
Set of models and their descriptions in different formats. Plus scripts to convert and collect the world.  

#Collect your world without pain!
No ROS required!

## Run
```gazebo result.world```

Or better (paused and verbose):

```gazebo -u result.world --verbose```

## Environment configuration
By default gazebo searches for the models in ~/.gazebo/models folder. 
You can add the path to custom models directory (for example to manipulators 
if you stay in the root of the project in terminal):  
```$ export GAZEBO_MODEL_PATH=${GAZEBO_MODEL_PATH}:$(pwd)/manipulators:$(pwd)/walking```

To check gazebo variables:  
```printenv | grep GAZEBO```

## urdf to gazebo model
```python3 urdf2model ```

## xacro to urdf
```$ xacro robot.xacro > robot.urdf ```

## check urdf on correctness
```$ check_urdf your_parallel_robot.urdf```

## urdf2sdf
```$ gz sdf -p robot.urdf > robot.sdf```

### TODO:
- more robots and examples
- support different versions


## robot descriptions and ideas

http://sachinchitta.github.io/urdf2/

http://sdformat.org/

https://github.com/rock-simulation/smurf_parser

http://wiki.ros.org/srdf

http://library.isr.ist.utl.pt/docs/roswiki/srdf.html

https://docs.nvidia.com/isaac/isaac_sim/plugins/robot_builder/urdf.html


## possible issues:
- if urdf has ros plugin it successfully converts to sdf and gazebo will fail to run  
- if you see next message, check the path to mesh files: 
  ```gzclient: /build/ogre-1.9-B6QkmW/ogre-1.9-1.9.0+dfsg1/OgreMain/include/OgreAxisAlignedBox.h:252: void Ogre::AxisAlignedBox::setExtents(const Ogre::Vector3&, const Ogre::Vector3&): Assertion `(min.x <= max.x && min.y <= max.y && min.z <= max.z) && "The minimum corner of the box must be less than or equal to maximum corner"' failed.```
- black screen in the gazebo means the model or mesh was not found ( check path to the model or GAZEBO_MODEL_PATH )
- if you do not understand why the gazebo can't find meshes or something other - check default models folder (.gazebo/models) that there are no robots with the same name. 