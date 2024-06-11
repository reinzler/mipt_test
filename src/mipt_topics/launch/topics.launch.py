from launch_ros.actions import Node
from launch import LaunchDescription


def generate_launch_description():

    # Launch main emergency script
    main_script_launch = Node(package='mipt_topics',
                              executable='main_script',
                              name='emergency_stop',
                              # namespace='my_namespace',
                              output='screen')

    return LaunchDescription([main_script_launch])