# 2-finger custom robot

## This package contains a custom robot moving in 2D with a 2-finger gripper for some tests.

<img src="imgs/custom_robot.png" width="200"/>

Dependencies:

- [Gazebo MimicJointPlugin](https://github.com/roboticsgroup/roboticsgroup_upatras_gazebo_plugins)
- [Gazebo contact_republisher](https://github.com/wonwon0/gazebo_contact_republisher)

After installation launch the basic environment using the following command:
```
roslaunch custom_robot pr_robot.launch
```

In order to use the contact sensor, install the gazebo_contact_republisher package and run in a new command line:
```
rosrun contact_republisher contact_republisher_node
```

The code scripts/contact_msg_counter.py transforms the gazebo contact message to a "custom" ros message.
