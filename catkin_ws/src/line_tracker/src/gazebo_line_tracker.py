#!/usr/bin/env python
import rospy
import numpy as np
import cv2
from std_msgs.msg import Float64
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import math
import time

current_yaw = 0
cv_image = 0
YAW_VARIANCE = .017
rospy.init_node('line_tracker', anonymous=False)

def yaw_callback(msg):
    global current_yaw
    current_yaw = msg.data

def camera_callback(camera_msg):
    bridge = CvBridge()
    global cv_image
    cv_image = bridge.imgmsg_to_cv2(camera_msg, "bgr8")


pub = rospy.Publisher('/yaw_control/setpoint', Float64, queue_size=10)

rospy.Subscriber('/leviathan/leviathan/camerabottom/camera_image', Image, camera_callback)


while(True):
    if type(cv_image) == int:
        continue 

    # Capture the frames
    frame = cv_image
    # Convert to grayscale
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # change from bgr values to hsv values
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # color bounds of color to be filtered out
    lower_color_bounds = np.array([100, 100, 0])
    upper_color_bounds = np.array([255, 255, 255])
    # mask shows in black the pixels being filtered out
    mask = cv2.inRange(hsv, lower_color_bounds, upper_color_bounds)
    # videofeed without filtered color
    res = cv2.bitwise_and(frame, frame, mask = mask)

    # Gaussian blur
    blur = cv2.GaussianBlur(mask,(5,5),0)
    # Color thresholding
    ret,thresh = cv2.threshold(blur,60,255,cv2.THRESH_BINARY_INV)
    # Find the contours of targeted color
    contours,hierarchy = cv2.findContours(mask, 1, cv2.CHAIN_APPROX_NONE)
    # Find the biggest contour (if detected)
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)

        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])

        cv2.line(res,(cx,0),(cx,720),(255,0,0),1)#vertical line
        cv2.line(res,(0,cy),(1280,cy),(255,0,0),1)#horizontal line
        cv2.drawContours(res, contours, -1, (0,255,0), 1)#line enclosing area identified to be the line

        #highest x-coordinate: 638
        #highest y-coordinate: 478
        #highest x and y coordinates may or may not be different for different cameras

        cx = cx - 319
        cy = 478 - cy

        #print("Coordinates: ", cx, cy)

        if cx == 0:
            radians = 0
        elif cy <= 0:
            radians = math.pi / 2
            if cx < 0:
                radians *= -1
        else:
            radians = math.atan2(cx, cy)

        #if abs(radians) < YAW_VARIANCE:
        #    continue

        rospy.Subscriber('/yaw_control/state', Float64, yaw_callback)
        radians = radians + current_yaw

        rospy.loginfo(radians)
        pub.publish(radians)
        time.sleep(.5)

    else:
        print("Line can not be detected\n")
 
    #Display the resulting frame

    cv2.imshow('original frame',frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

