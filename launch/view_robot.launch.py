import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node
import xacro

def generate_launch_description():
    robotXacroName='robot'
    namePackage='diffy'
    modelFileRelativePath='models/urdf/robot.xacro'
    pathModelFile=os.path.join(get_package_share_directory(namePackage),modelFileRelativePath)
    
    robotDescription=xacro.process_file(pathModelFile).toxml()
    
    nodeRobotStatePublisher=Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[
            {'robot_description': robotDescription, 'use_sim_time': True},
        ],
    )
    
    nodejointStatePublisher=Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        output='screen',
    )
        
    launchDescriptionObject=LaunchDescription()
    launchDescriptionObject.add_action(nodeRobotStatePublisher)
    launchDescriptionObject.add_action(nodejointStatePublisher)
    
    return launchDescriptionObject