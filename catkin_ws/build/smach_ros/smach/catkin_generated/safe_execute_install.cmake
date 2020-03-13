execute_process(COMMAND "/home/jack/RoboSub/catkin_ws/build/smach_ros/smach/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/jack/RoboSub/catkin_ws/build/smach_ros/smach/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
