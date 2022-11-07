cmake_minimum_required(VERSION 3.0.2)
project(custom_robot)


find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  controller_manager
  effort_controllers
  gazebo_ros
  gazebo_ros_control
  joint_state_controller
  joint_trajectory_controller
  robot_state_publisher
  moveit_kinematics
  robotiq_2f_c2_gripper_visualization
)
catkin_package( CATKIN_DEPENDS
  robotiq_2f_c2_gripper_visualization

)


include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)
