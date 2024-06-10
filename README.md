```
ros2 topic pub --once /stop_cmd_park std_msgs/msg/Int8 "{data: 0}"
ros2 topic pub /stop_cmd_park std_msgs/msg/Int8 "{data: 1}"
ros2 topic pub /stop_cmd_park std_msgs/msg/Int8 "{data: 0}"
```