"""
gazebo_link.py: redirects the ROS topics from Gazebo to Seadragon:
                  - continuously subscribes to Gazebo sensor topics, publishes to Seadragon
                  - continuously subscribes to Seadragon thruster topics, publishes to Gazebo
"""

import rospy
from std_msgs.msg import Bool, Float64, Int16, String, Header
from sensor_msgs.msg import FluidPressure, MagneticField, Imu, Image
from uuv_gazebo_ros_plugins_msgs.msg import FloatStamped
import time
import math
import numpy as np
import tf


class SimLink():

    PWM_SCALING = 8  # how much to scale yaw_pwm and depth_pwm by for the Gazebo thrusters

    def __init__(self):
        # class-wide current yaw PWM values
        self.leviathanThrusterYawPwm = 0

        # get ROS publishers and subscribers
        self.seadragonPressurePub = rospy.Publisher('/depth', Int16, queue_size=10)  # Seadragon depth
        self.seadragonMagnetometerPub = rospy.Publisher('/magnetometer', Float64, queue_size=10)  # Seadragon magnetometer
        self.seadragonImuPub = rospy.Publisher('/imu/data', Imu, queue_size=10)  # Seadragon magnetometer
        self.seadragonCameraFrontPub = rospy.Publisher('/camerafront/camera_image', Float64, queue_size=10)  # Seadragon camera front
        self.seadragonCameraBottomPub = rospy.Publisher('/camerabottom/camera_image', Float64, queue_size=10)  # Seadragon camera bottom
        self.seadragonDepthPwm = rospy.Publisher('/depth_pwm', Int16, queue_size=10)  # Seadragon depth PWM

        self.gazeboPressureSub = rospy.Subscriber('/leviathan/pressure', FluidPressure, self.gazeboPressureCallback)  # Gazebo depth
        self.gazeboMagnetometerSub = rospy.Subscriber('/leviathan/magnetometer', MagneticField, self.gazeboMagnetometerCallback)  # Gazebo magnetometer
        self.gazeboImuSub = rospy.Subscriber('/leviathan/imu', Imu, self.gazeboImuCallback)  # Gazebo Imu
        self.gazeboCameraFrontSub = rospy.Subscriber('/leviathan/leviathan/camerafront/camera_image', Image, queue_size=10)  # Gazebo camera front
        self.gazeboCameraBottomSub = rospy.Subscriber('/leviathan/leviathan/camerabottom/camera_image', Image, queue_size=10)  # Gazebo camera bottom
        self.gazeboCameraBottomSub = rospy.Subscriber('/leviathan/leviathan/camerabottom/camera_image', Image, queue_size=10)  # Gazebo camera bottom
        self.seadragonDepthPwmFeedback = rospy.Subscriber('/depth_pwm_feedback', Int16, self.seadragonDepthPwmFeedbackCallback)  # Seadragon Depth PWM Feedback (from Dynamic Reconfigure)
        self.seadragonYawPwmFeedback = rospy.Subscriber('/yaw_pwm_feedback', Int16, self.seadragonYawPwmFeedbackCallback)  # Seadragon Yaw PWM Feedback (from Dynamic Reconfigure)

        self.leviathanYawPwmSub = rospy.Subscriber('/yaw_pwm/', Int16, self.leviathanThrusterYawPwmCallback)  # Leviathan Yaw PWM

        self.gazeboThrusterYawFrontLeftPub = rospy.Publisher('/leviathan/thrusters/0/input', FloatStamped, queue_size=10)  # Gazebo thruster yaw front-left
        self.gazeboThrusterYawFrontRightPub = rospy.Publisher('/leviathan/thrusters/1/input', FloatStamped, queue_size=10)  # Gazebo thruster yaw front-right
        self.gazeboThrusterYawBackLeftPub = rospy.Publisher('/leviathan/thrusters/2/input', FloatStamped, queue_size=10)  # Gazebo thruster yaw back-left
        self.gazeboThrusterYawBackRightPub = rospy.Publisher('/leviathan/thrusters/3/input', FloatStamped, queue_size=10)  # Gazebo thruster yaw back-right

        self.gazeboThrusterDepthFrontLeftPub = rospy.Publisher('/leviathan/thrusters/4/input', FloatStamped, queue_size=10)  # Gazebo thruster depth front-left
        self.gazeboThrusterDepthFrontRightPub = rospy.Publisher('/leviathan/thrusters/5/input', FloatStamped, queue_size=10)  # Gazebo thruster depth front-right
        self.gazeboThrusterDepthBackLeftPub = rospy.Publisher('/leviathan/thrusters/6/input', FloatStamped, queue_size=10)  # Gazebo thruster depth back-left
        self.gazeboThrusterDepthBackRightPub = rospy.Publisher('/leviathan/thrusters/7/input', FloatStamped, queue_size=10)  # Gazebo thruster depth back-right

        self.seadragonThrusterDepthFrontLeftSub = rospy.Subscriber('/depth_pwm/', Int16, self.seadragonThrusterDepthFrontLeftCallback)  # Seadragon thruster depth front-left
        self.seadragonThrusterDepthFrontRightSub = rospy.Subscriber('/depth_pwm/', Int16, self.seadragonThrusterDepthFrontRightCallback)  # Seadragon thruster depth front-right
        self.seadragonThrusterDepthBackLeftSub = rospy.Subscriber('/depth_pwm/', Int16, self.seadragonThrusterDepthBackLeftCallback)  # Seadragon thruster depth back-left
        self.seadragonThrusterDepthBackRightSub = rospy.Subscriber('/depth_pwm/', Int16, self.seadragonThrusterDepthBackRightCallback)  # Seadragon thruster depth back-right

        print("Redirecting topics...")
    

    # callbacks: when a topic is published, the respective function is called
    def gazeboPressureCallback(self, msg):  # returns depth in inches
        self.seadragonPressurePub.publish(Int16((msg.fluid_pressure - 107) / 1.1))

    def gazeboMagnetometerCallback(self, msg):
        magnetometer_orientation = math.atan(msg.magnetic_field.y / msg.magnetic_field.x) * -2
        self.seadragonMagnetometerPub.publish(magnetometer_orientation)

    def gazeboImuCallback(self, msg):
        q = np.array([msg.orientation.x, msg.orientation.y, msg.orientation.z, msg.orientation.w])
        orientation = tf.transformations.euler_from_quaternion(q)
        self.imu_data = orientation[2] # for debug
        self.seadragonImuPub.publish(msg)

    def gazeboCameraFrontCallback(self, msg):
        self.seadragonCameraFrontPub.publish(msg.data)

    def gazeboCameraBottomCallback(self, msg):
        self.seadragonCameraBottomPub.publish(msg.data)

    def seadragonDepthPwmFeedbackCallback(self, msg):
        self.seadragonDepthPwm.publish(msg.data * -1)

    def leviathanThrusterYawPwmCallback(self, msg):
        self.leviathanThrusterYawPwm = msg.data
        print("Yaw Set To: " + str(msg.data))
        self.gazeboThrusterYawFrontLeftPub.publish(FloatStamped(data=msg.data * self.PWM_SCALING))
        self.gazeboThrusterYawFrontRightPub.publish(FloatStamped(data=msg.data * self.PWM_SCALING))
        self.gazeboThrusterYawBackLeftPub.publish(FloatStamped(data=msg.data * -1 * self.PWM_SCALING))
        self.gazeboThrusterYawBackRightPub.publish(FloatStamped(data=msg.data * -1 * self.PWM_SCALING))

    def seadragonYawPwmFeedbackCallback(self, msg):
        self.gazeboThrusterYawFrontLeftPub.publish(FloatStamped(data=self.leviathanThrusterYawPwm + msg.data * self.PWM_SCALING))
        self.gazeboThrusterYawFrontRightPub.publish(FloatStamped(data=self.leviathanThrusterYawPwm - msg.data * self.PWM_SCALING))
        self.gazeboThrusterYawBackLeftPub.publish(FloatStamped(data=self.leviathanThrusterYawPwm - msg.data * self.PWM_SCALING))
        self.gazeboThrusterYawBackRightPub.publish(FloatStamped(data=self.leviathanThrusterYawPwm + msg.data * self.PWM_SCALING))
        print(str(self.leviathanThrusterYawPwm + msg.data * self.PWM_SCALING) + " | " + str(self.imu_data))

    def seadragonThrusterDepthFrontLeftCallback(self, msg):
        self.gazeboThrusterDepthFrontLeftPub.publish(FloatStamped(data=msg.data * self.PWM_SCALING))
    
    def seadragonThrusterDepthFrontRightCallback(self, msg):
        self.gazeboThrusterDepthFrontRightPub.publish(FloatStamped(data=msg.data * self.PWM_SCALING))

    def seadragonThrusterDepthBackLeftCallback(self, msg):
        self.gazeboThrusterDepthBackLeftPub.publish(FloatStamped(data=msg.data * self.PWM_SCALING))
    
    def seadragonThrusterDepthBackRightCallback(self, msg):
        self.gazeboThrusterDepthBackRightPub.publish(FloatStamped(data=msg.data * self.PWM_SCALING))
    
if __name__ == "__main__":
    rospy.init_node("gazebo_link")  # init ros node
    rate = rospy.Rate(20)
    link = SimLink()
    while not rospy.is_shutdown(): # main loop
        rate.sleep()
