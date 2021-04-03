# thrusterDriver.py (v2)

# file used as a template: gateTask.py
# GitHub: https://raw.githubusercontent.com/robosub-ucr/LeviathanAUV/master/catkin_ws/src/Mission%20Control/competition_tasks/src/gateTask.py
#!/usr/bin/env python



import rospy
import smach
import smach_ros
from std_msgs.msg import Bool, Float64, Int16


class ThrusterDriver():
  
  PWMBASELINE = 1500
  
  def __init__(self): # like a constructor in python
  
    # all publishers
    # EXAMPLE: self. = rospy.Publisher('/depth', Int16, queue_size=10)  # Seadragon depth
    self.depth_all_pub = rospy.Publisher('/depth_thrust', Int16, queue_size=10) # the topic 'depth_thrust' is published, with type "Int16", for all 4 motors; this publisher is named "depth_all_pub"
    self.thrust_FR_pub = rospy.Publisher('/FR_thrust', Int16, queue_size=10)
    self.thrust_FL_pub = rospy.Publisher('/FL_thrust', Int16, queue_size=10)
    self.thrust_BR_pub = rospy.Publisher('/BR_thrust', Int16, queue_size=10)
    self.thrust_BL_pub = rospy.Publisher('/BL_thrust', Int16, queue_size=10)
    
    #all subscribers
    self.depthMotorSub = rospy.Subscriber('/depth_pwm', Int16, self.depth_callback)  # the function "depth_callback" subscribes to the topic '/depth_pwm', which is type "Int16"; this subscriber is named "depthMotorSub"
    self.depthFeedbackSub = rospy.Subscriber('/depth_pwm_feedback', Int16, self.depth_feedback_callback)
    self.forwardMotorSub = rospy.Subscriber('/yaw_pwm', Int16, self.forward_callback) #yaw_pwm isn't ideal, placeholder for now; forward_pwm would be a better name to change it to
    self.yawFeedbackSub = rospy.Subscriber('/yaw_pwm_feedback', Int16, self.yaw_feedback_callback)
    self.strafeMotorSub = rospy.Subscriber('/strafe_pwm', Int16, self.strafe_callback) #WIP
    
 
  # Dimitri's code below
    self.depth_all_pwm = self.PWMBASELINE

    self.tempo_thrust_FR = 0
    self.tempo_thrust_FL = 0
    self.tempo_thrust_BR = 0
    self.tempo_thrust_BL = 0

  
  # Depth movement up/down
  def depth_callback(self, msg): #tag-depth  
    if msg.data == 0: # stop motors
      self.depth_all_pwm = self.PWMBASELINE  
    elif msg.data < 0: # reverse-thrust motors
      self.depth_all_pwm = self.PWMBASELINE - 25 + msg.data
    else: # forward-thrust motors
         self.depth_all_pwm = self.PWMBASELINE + 25 + msg.data
  
    # Receives depth feedback vallues from [0:50]
  def depth_feedback_callback(self, msg): #tag-depth
    # depth feedback control
    tempo = 0
    if (msg.data > 1):
      tempo = 25 + msg.data
    else if (msg.data < -1):
      tempo = -25 + msg.data   
    self.depth_all_pwm += tempo

   # thrust_FR front right, thrust_RL rear left etc.
  def forward_callback(self, msg): #tag-yaw    
    if msg.data == 0:
      self.tempo_thrust_FR = self.tempo_thrust_FL = self.tempo_thrust_BR = self.tempo_thrust_BL = 0
    else:
      if msg.data < 0: # Go reverse
        tempo = - 29 + msg.data
      else: # Go forward
        tempo = 29 + msg.data
      self.tempo_thrust_FR += tempo
      self.tempo_thrust_FL += tempo
      self.tempo_thrust_BR += tempo
      self.tempo_thrust_BL += tempo

   # turning left-right
   # I assume that positive msg.data means turn left. If not just switch motor variables
  def yaw_feedback_callback(self, msg): #tag-yaw
    if self.tempo_thrust_FR == 0: #currently all thrusters are changed together so any one can be used to check
      if abs(msg.data > 0.25)
        if (msg.data > 0.25):#turn left
          tempo = msg.data + 29
        else: #turn right
          tempo = msg.data - 29
        self.tempo_thrust_FL -= tempo
        self.tempo_thrust_BL -= tempo
        self.tempo_thrust_FR += tempo
        self.tempo_thrust_BR += tempo
    else:   #Motors are on
      self.tempo_thrust_FL -= msg.data
      self.tempo_thrust_BL -= msg.data
      self.tempo_thrust_FR += msg.data
      self.tempo_thrust_BR += msg.data     

   # strafe left/right
   #assume that positive msg.data means strafe right
  def strafe_callback(self, msg):
    if msg.data != 0:
      if msg.data < 0: #strafe left
        tempo = -25 + msg.data # msg.data is negative in this elif case, so (-25 + msg.data) is overall negative;
      else: # strafe right
        tempo = 25 + msg.data
      self.tempo_thrust_FL += tempo
      self.tempo_thrust_BR += tempo
      self.tempo_thrust_FR -= tempo
      self.tempo_thrust_BL -= tempo
      
  def execute(self):
    if self.depth_all_pwm > 1800:
      self.depth_all_pwm = 1800
    elif self.depth_all_pwm < 1200:
      self.depth_all_pwm = 1200
      
    tempo_thrust_all = [self.tempo_thrust_FR, self.tempo_thrust_FL, self.tempo_thrust_BR, self.tempo_thrust_BL]
    final_thrust_all = []
    for item in tempo_thrust_all:
      if abs(item) > 300:
        if item > 300:
          tempo = 300
        else:
          tempo = -300
      else:
        tempo = item
      final_thrust_all.append(tempo + self.PWMBASELINE)
    
    #publish final values
    pub_msg = Int16() # create new Int16() wrapper object, which is the message to be sent
    pub_msg.data = self.depth_all_pwm # access the data member variable of the message object, and assign its value
    self.depth_all_pub.publish(pub_msg) # publish the message object called "depth_msg" to ROS, for other programs to read
    
    # Alternate method of publishing below, with IntStamped() function call, using inline declaration of the messsage object
    #self.thrust_FR_pub.publish(IntStamped(data=self.final_thrust_FR)) # makes 32-bit Int message, and publishes it, according to documentation

    pub_msg.data = final_thrist_all[0]
    self.thrust_FR_pub.publish(pub_msg)
    pub_msg.data = final_thrist_all[1]
    self.thrust_FL_pub.publish(pub_msg)
    pub_msg.data = final_thrist_all[2]
    self.thrust_BR_pub.publish(pub_msg)
    pub_msg.data = final_thrist_all[3]
    self.thrust_BL_pub.publish(pub_msg)
    
    
if __name__ == "__main__":
  rospy.init_node("thruster_driver")  # init ros node
  rate = rospy.Rate(20)
  driver = ThrusterDriver()
  while not rospy.is_shutdown(): # main loop
    driver.execute()
    rate.sleep()
    

