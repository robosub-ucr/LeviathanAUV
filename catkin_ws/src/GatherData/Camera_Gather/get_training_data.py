#!/usr/bin/env python

import rospy
import time
import cv2
import os
import numpy as np
import sys, select, termios, tty
from readinput import getKey, checkKey
from sensor_msgs.msg import Image
 

rospy.init_node('image_pub') 

global record
record = False

settings = termios.tcgetattr(sys.stdin)


############################


############################
		

############################
	
	
############################

cap = cv2.VideoCapture(0)

i = 0

image_publisher = rospy.Publisher('/camera/rgb/image_raw', Image, queue_size=10)

while True:
	
	ret, image = cap.read()
	pub = Image
	cv2.imshow('Seadragon view', image)
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
		image = cv2.resize(image,(400,300))
		if(i % 5 == 0):
			pub.data = image
			image_publisher.publish(pub)		
			cv2.imwrite('data/image' + str(i) + '.png', image)
		i = i + 1

cap.release()
cv2.destroyAllWindows()
