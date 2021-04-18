# robot_shop
Set of models and their descriptions in different formats. Plus scripts to convert and collect the world.  

#Collect your world without pain!
No ROS required!

## Run
```gazebo result.world```

## Environment configuration
By default gazebo searches for the models in ~/.gazebo/models folder. 
You can add the path to custom models directory (for example to the root of this project 
if you stay there in terminal):  
```$ export GAZEBO_MODEL_PATH=${GAZEBO_MODEL_PATH}:$(pwd)```

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

## issues:
- if urdf has ros plugin it successfully converts to sdf and gazebo will fail to run  
- seems gazebo searches only in default models if you include by one level: models://robot_model . 
  But include from custom directory is working if you specify two levels:  models://subfolder/robot_model

## foundations:
black screen in gazebo means model not found ( check path to model )
no robot - check uri in sdf (meshes not found)

## robot descriptions and ideas

http://sachinchitta.github.io/urdf2/
http://sdformat.org/
https://github.com/rock-simulation/smurf_parser
http://wiki.ros.org/srdf
http://library.isr.ist.utl.pt/docs/roswiki/srdf.html
https://docs.nvidia.com/isaac/isaac_sim/plugins/robot_builder/urdf.html
