To download, build and launch the package:

```
git clone https://github.com/reinzler/mipt_test.git
cd mipt_test
colcon build && source install/local_setup.bash
ros2 launch mipt_topics topics.launch.py
```

Test commands:
```
ros2 topic pub --once /test/stop_cmd_park std_msgs/msg/Int8 "{data: 0}"
ros2 topic pub /test/stop_cmd_park std_msgs/msg/Int8 "{data: 1}"
ros2 topic pub /test/stop_cmd_park std_msgs/msg/Int8 "{data: 0}"
```

To check current ROS_DOMAIN:
```
echo $ROS_DOMAIN_ID - if it return nothing, ID=0
```

To run the script in specific ROS_DOMAIN:
```
ros2 run mipt_topics mipt_topics.py --ros-args -r __ros_domain_id:=42
```
To be able to see nodes, topics running in the specific ROS_DOMAIN:
```
export ROS_DOMAIN_ID=42
```