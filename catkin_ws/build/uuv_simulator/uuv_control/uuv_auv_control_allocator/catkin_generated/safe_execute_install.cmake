execute_process(COMMAND "/home/richard/LeviathanAUV/catkin_ws/build/uuv_simulator/uuv_control/uuv_auv_control_allocator/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/richard/LeviathanAUV/catkin_ws/build/uuv_simulator/uuv_control/uuv_auv_control_allocator/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
