# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include".split(';') if "${prefix}/include" != "" else []
PROJECT_CATKIN_DEPENDS = "roscpp;gazebo_msgs;geometry_msgs;uuv_world_plugins;uuv_world_ros_plugins_msgs;gazebo_dev".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-luuv_underwater_current_ros_plugin;-luuv_sc_ros_interface_plugin".split(';') if "-luuv_underwater_current_ros_plugin;-luuv_sc_ros_interface_plugin" != "" else []
PROJECT_NAME = "uuv_world_ros_plugins"
PROJECT_SPACE_DIR = "/home/richard/catkin_ws/install"
PROJECT_VERSION = "0.6.13"
