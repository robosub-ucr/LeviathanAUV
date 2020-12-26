#!/usr/bin/env python

import rospy
import time
import cv2
import os
import numpy as np
import sys, select, termios, tty
from readinput import getKey, checkKey
from sensor_msgs.msg import Image
 
from cv_bridge import CvBridge, CvBridgeError

import math

import time


rospy.init_node('image_pub') 

global record
record = False

settings = termios.tcgetattr(sys.stdin)

cv_image = 0
############################


############################
		

############################
	
	
############################

cap = cv2.VideoCapture(0)

i = 0

def camera_callback(camera_msg):
	bridge = CvBridge()
	global cv_image
	cv_image = bridge.imgmsg_to_cv2(camera_msg, "bgr8")


image_publisher = rospy.Publisher('/camera/rgb/image_raw', Image, queue_size=10)
rospy.Subscriber('/leviathan/leviathan/camerafront/camera_image', Image, camera_callback)

while True:
	
	#ret, image = cap.read()
	#pub = Image
	cv2.imshow('Seadragon view', cv_image)
	cv2.waitKey(1)	
	
	# Read user input 	
	key = getKey(settings)

	# Stop or Start recording data
	
	if (key == "p"):
		record = False

	elif(key == "r"):
		record = True
	elif(key == "q"):
		break
	#if(key == "r"):
	#	record = True
	#else:
	#	record = False

	if not record:
		print ("Paused Recording Data")
	else:
		# Record Data
		print ("Recording Data")
		#image = cv2.resize(image,(400,300))
		if(i % 5 == 0):
			#pub.data = image
			#image_publisher.publish(pub)		
			cv2.imwrite('data/image' + str(i) + '.png', cv_image)
		i = i + 1

cap.release()
cv2.destroyAllWindows()
