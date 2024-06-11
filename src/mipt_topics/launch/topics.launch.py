from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import SetEnvironmentVariable


def generate_launch_description():
    # Launch main emergency script
    main_script_launch = Node(package='mipt_topics',
                              executable='main_script',
                              name='emergency_stop',
                              # namespace='my_namespace',
                              output='screen')

    # To launch the node in specific ROS_DOMAIN, for example in 42:
    # return LaunchDescription([SetEnvironmentVariable('ROS_DOMAIN_ID', '42'), main_script_launch])

    # Simply launch node in default ROS_DOMAIN (0)
    return LaunchDescription([main_script_launch])
