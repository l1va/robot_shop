# robot_shop
Set of models and their descriptions in different formats

#Collect your world without pain!

## Environment configuration
By default gazebo searches for the models in ~/.gazebo/models folder. 
You can add the path to models by (for example):  
```$ export GAZEBO_MODEL_PATH=${GAZEBO_MODEL_PATH}:$(pwd)/manipulators```

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
