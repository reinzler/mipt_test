from launch_ros.actions import Node
from launch import LaunchDescription


def generate_launch_description():

    # Launch main emergency script
    main_script_launch = Node(package='mipt',
                              executable='main_script',
                              # name='emergency_stop',
                              output='screen')

    return LaunchDescription([main_script_launch])