import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8


class EmergencyStopNode(Node):
    def __init__(self, namespace: str):
        super().__init__('emergency_stop_node', namespace=namespace)

        # Lets create subscribers for all 4 topics:
        self.stop_cmd_park_subscriber = self.create_subscription(Int8,
                                                                 f"/{namespace}/stop_cmd_park",
                                                                 self.stop_cmd_park_callback,
                                                                 qos_profile=10)
        self.stop_cmd_human_subscriber = self.create_subscription(Int8,
                                                                  f"/{namespace}/stop_cmd_human",
                                                                  self.stop_cmd_human_callback,
                                                                  qos_profile=10)
        self.stop_cmd_robot_subscriber = self.create_subscription(Int8,
                                                                  f"/{namespace}/stop_cmd_robot",
                                                                  self.stop_cmd_robot_callback,
                                                                  qos_profile=10)
        self.stop_cmd_belt_subscriber = self.create_subscription(Int8,
                                                                 f"/{namespace}/stop_cmd_belt",
                                                                 self.stop_cmd_belt_callback,
                                                                 qos_profile=10)

        """
        Now create publisher for /stop_cmd topic, if we will receive stop command from at least one topic, will publish
        stop command to /stop_cmd topic ("0")
        """
        self.emergency_stop = self.create_publisher(Int8, f"/{namespace}/stop_cmd", 10)
        self.emergency_signal = self.create_publisher(Int8, "/beep", 10)

        # Now create flags for all topics
        self.stop_cmd_park, self.stop_cmd_human, self.stop_cmd_robot, self.stop_cmd_belt = True, True, True, True

    def stop_cmd_park_callback(self, msg):
        if msg.data == 0:
            self.stop_cmd_park = False
            msg_signal = Int8()
            msg_signal.data = 0
            self.emergency_signal.publish(msg_signal)
        else:
            self.stop_cmd_park = True
        self.check_if_can_continue_movement()

    def stop_cmd_human_callback(self, msg):
        if msg.data == 0:
            self.stop_cmd_human = False
            msg_signal = Int8()
            msg_signal.data = 1
            self.emergency_signal.publish(msg_signal)
        else:
            self.stop_cmd_human = True
        self.check_if_can_continue_movement()

    def stop_cmd_robot_callback(self, msg):
        if msg.data == 0:
            self.stop_cmd_robot = False
        else:
            self.stop_cmd_robot = True
        self.check_if_can_continue_movement()

    def stop_cmd_belt_callback(self, msg):
        if msg.data == 0:
            self.stop_cmd_belt = False
            msg_signal = Int8()
            msg_signal.data = 2
            self.emergency_signal.publish(msg_signal)
        else:
            self.stop_cmd_belt = True
        self.check_if_can_continue_movement()

    def check_if_can_continue_movement(self):
        move_msg = Int8()
        emergency_break = all([self.stop_cmd_park, self.stop_cmd_human, self.stop_cmd_robot, self.stop_cmd_belt])
        if emergency_break:
            move_msg.data = 1
            for _ in range(3):
                self.emergency_stop.publish(move_msg)

        else:
            move_msg.data = 0
            self.emergency_stop.publish(move_msg)


def main(args=None):
    rclpy.init(args=args)
    emergency_stop = EmergencyStopNode(namespace='test')
    rclpy.spin(emergency_stop)
    emergency_stop.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
