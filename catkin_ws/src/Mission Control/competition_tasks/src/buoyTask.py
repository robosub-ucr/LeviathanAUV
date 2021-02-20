#!/usr/bin/env python

import numpy as np
import rospy
import smach
import smach_ros
from std_msgs.msg import Bool, Float64, Int16

import seadragon_states as sd
import time

CAMERA_WIDTH = 400
CAMERA_HEIGHT = 300
CENTER_PADDING_X = 15
CENTER_PADDING_Y = 15
YAW_INCREASE = 0.017 # radians
DEPTH_STEP = 1
FORWARD_THRUST_INCREASE = 60
AREA_THRESHOLD_LOW = 0.15
AREA_THRESHOLD_HIGH = 0.2
TORPEDO_Y_OFFSET = 10
MAX_FORWARD_THRUST= 120

#KEEP
class StartState(smach.State):
  def __init__(self):
    smach.State.__init__(self, outcomes=['ready', 'notready'])

    self.enabled = False
    rospy.Subscriber('/buoy_enable', Bool, self.enabled_callback)

  def enabled_callback(self, msg):
    self.enabled = msg.data

  def execute(self, userdata):
    if self.enabled:
      self.enabled = False
      return 'ready'
    else:
      return 'notready'

# KEEP THIS STATE
class RotateYawState(smach.State):
  def __init__(self, yaw_change, variance):
    smach.State.__init__(self, outcomes=['done', 'notdone', 'reset'])

    self.yaw_published = False
    self.yaw_change = yaw_change
    self.yaw_variance = variance
    self.yaw_target = Float64()
    self.timer = 0

    self.yaw_current = 0 # in degrees, None if the callback hasnt triggered yet
    rospy.Subscriber('/yaw_control/state', Float64, self.yaw_callback) # current orientation
    self.yaw_publisher = rospy.Publisher('/yaw_control/setpoint', Float64, queue_size=10) # desired orientation

    self.has_reset = False
    self.reset_subscriber = rospy.Subscriber('/reset', Bool, self.reset_callback)

  def yaw_callback(self, msg):
    self.yaw_current = msg.data
  def reset_callback(self, msg):
    self.has_reset = msg.data

  def execute(self, userdata):
    print("yaw_state", self.yaw_current, "yaw_setpoint", self.yaw_current + self.yaw_change)
    if self.has_reset:
      self.resetValues()
      return 'reset'

    self.timer += 1
    if not self.yaw_published: #todo: find way to print that self.yaw_published = True
      self.yaw_target.data = self.yaw_current + self.yaw_change
      self.yaw_publisher.publish(self.yaw_target)
      self.yaw_published = True
      return 'notdone'
    elif abs(self.yaw_current - self.yaw_target.data) < self.yaw_variance:
			return 'done'
    else:
			return 'notdone'

  def resetValues(self):
    self.yaw_current = 0
    self.has_reset = False
    self.yaw_published = False
    self.timer = 0

# keep main()
def main():
  rospy.init_node('buoy_task_state_machine')
  sm = smach.StateMachine(outcomes=['buoy_task_complete'])
  sis = smach_ros.IntrospectionServer('server_name', sm, '/SM_ROOT')
  sis.start()

  buoy_flat_topic = {
    'x': '/buoy_flat_x',
    'y': '/buoy_flat_y',
    'area': '/buoy_flat_area'
  }

  buoy_triangle_topic = {
    'x': '/buoy_triangle_x',
    'y': '/buoy_triangle_y',
    'area': '/buoy_triangle_area'
  }

  TOUCH_FLAT_TIMER 	= 10000 # time required (in ticks) to touch the flat buoy
  MOVE_BACK_1_TIMER 	= 6000  # time required (in ticks) to move back, away from flat buoy
  MOVE_FORWARD_TIMER 	= 10000 # time required (in ticks) to move past the flat buoy
  TOUCH_TRIANGLE_TIMER = 10000 # time required (in ticks) to touch the triangle buoy
  MOVE_BACK_2_TIMER 	= 6000 # time required (in ticks) to move back, away from triangle buoy

  BUOY_ABOVE_DEPTH 	= 2*12  # Adjusts sub to move 2 ft up
  BUOY_BELOW_DEPTH 	= 3.5*12   # Adjusts sub to move 3.5 ft down
  TORPEDO_BOARD_DEPTH = 3*12   # Adjusts sub to move 3 ft down
  DEPTH_VARIANCE 		= 2    # 2 inch

  YAW_BUOY_BACK 		= 3.14 # the yaw (in radians) to make sub turn 180 degrees to face back buoys
  YAW_TORPEDO_TASK 	= 0.5  # the yaw (in radians) to face the torpedo task
  YAW_VARIANCE 		= 0.1  # in radians

  with sm: # This where states will get added to the State Machine
    smach.StateMachine.add('IDLE', StartState(), # this function is used to be added as a state to the SM
      transitions={'ready':'TOUCH_FLAT', 'notready':'IDLE'})

    smach.StateMachine.add('TOUCH_FLAT', sd.MoveForwardTimed(TOUCH_FLAT_TIMER, True), # MoveForwardTimed is a state from sd (seadragon_states.py)
      transitions={'done':'MOVE_BACK_1', 'notdone':'TOUCH_FLAT', 'reset':'RESET'})

    smach.StateMachine.add('MOVE_BACK_1', sd.MoveForwardTimed(MOVE_BACK_1_TIMER, False), 
      transitions={'done':'MOVE_UP', 'notdone':'MOVE_BACK_1', 'reset':'RESET'})

    smach.StateMachine.add('MOVE_UP', sd.ChangeDepthToTarget(BUOY_ABOVE_DEPTH), #24
      transitions={'done':'MOVE_FORWARD', 'notdone':'MOVE_UP', 'reset':'RESET'})

    smach.StateMachine.add('MOVE_FORWARD', sd.MoveForwardTimed(MOVE_FORWARD_TIMER, True), 
      transitions={'done':'MOVE_DOWN', 'notdone':'MOVE_FORWARD', 'reset':'RESET'})

    smach.StateMachine.add('MOVE_DOWN', sd.ChangeDepthToTarget(BUOY_BELOW_DEPTH), #42
      transitions={'done':'TURN_AROUND', 'notdone':'MOVE_DOWN', 'reset':'RESET'})

    smach.StateMachine.add('TURN_AROUND', sd.Rotate180(YAW_BUOY_BACK), 
      transitions={'done':'TOUCH_TRIANGLE', 'notdone':'TURN_AROUND', 'reset':'RESET'})

    smach.StateMachine.add('TOUCH_TRIANGLE', sd.MoveForwardTimed(TOUCH_TRIANGLE_TIMER, True), 
      transitions={'done':'MOVE_BACK_2', 'notdone':'TOUCH_TRIANGLE', 'reset':'RESET'})

    smach.StateMachine.add('MOVE_BACK_2', sd.MoveForwardTimed(MOVE_BACK_2_TIMER, False), 
      transitions={'done':'FACE_TORPEDO_TASK', 'notdone':'MOVE_BACK_2', 'reset':'RESET'})

    smach.StateMachine.add('FACE_TORPEDO_TASK', RotateYawState(YAW_TORPEDO_TASK, YAW_VARIANCE), 
      transitions={'done':'MOVE_TORPEDO_DEPTH', 'notdone':'FACE_TORPEDO_TASK', 'reset':'RESET'})

    smach.StateMachine.add('MOVE_TORPEDO_DEPTH', sd.ChangeDepthToTarget(TORPEDO_BOARD_DEPTH), 
      transitions={'done':'COMPLETED', 'notdone':'MOVE_TORPEDO_DEPTH', 'reset':'RESET'})

    smach.StateMachine.add('COMPLETED', sd.PublishTopic('/buoy_task_complete', True),
      transitions={'done':'IDLE'})

    smach.StateMachine.add('RESET', sd.Reset(), 
      transitions={'done':'IDLE'})

  outcome = sm.execute()
  rospy.spin()
  sis.stop()

if __name__ == '__main__':
  main()