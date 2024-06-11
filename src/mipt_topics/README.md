```
ros2 topic pub --once /stop_cmd_park std_msgs/msg/Int8 "{data: 0}"
```
```
ros2 topic pub /stop_cmd_park std_msgs/msg/Int8 "{data: 1}"
```
```
ros2 topic pub /stop_cmd_park std_msgs/msg/Int8 "{data: 0}"
```
```
colcon build && source install/local_setup.bash
ros2 launch mipt_topics topics.launch.py
ros2 run mipt_topics mipt_topics.py --ros-args -r __ros_domain_id:=42
```
ROS_DOMAIN_ID
```
export ROS_DOMAIN_ID=42
```
```
echo $ROS_DOMAIN_ID
```