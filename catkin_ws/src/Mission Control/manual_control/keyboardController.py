import rospy
import numpy as np
import pygame
import serial
from geometry_msgs.msg import Twist
from std_msgs.msg import String, Empty, Float64, Int16, Bool
pygame.init()
rospy.init_node('KeyboardController')

#---- initialize publishers/subscribers -----------------------------\\

#/cmd_vel is used for simulation
vel_msg = Twist() 
vel_msg.linear.x = 0  # meters per second
vel_msg.linear.y = 0  # meters per second
vel_msg.linear.z = 0  # meters per second
vel_msg.angular.z = 0  # radians per second
vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
print(vel_msg)

#/yaw_pwm is used for real(non sim) linear velocity
thrust_msg= Int16()
thrust_msg.data= 0
thrust_publisher= rospy.Publisher('/yaw_pwm', Int16, queue_size=10)
print(thrust_msg)

#/yaw_pwm_feedback is used for angular velocity, 
# publishes target angle, not the actual angular velocity, might need to subscribe to the ahrs topic
angVel_msg= Int16()
angVel_msg.data= 0
angVel_publisher= rospy.Publisher('/yaw_pwm_feedback', Int16, queue_size=10)
print(angVel_msg)

# linVel = 0
# angVel = 0
Max_linVel = 3
Max_angVel = 2
Max_pwm= 1500 + 250
x_cnt= 0
y_cnt= 0
z_cnt= 0
#0---------------------------------------------------------------------//


#----------------Joystick&KB_init-----------------------\\
js_connected= False
pygame.joystick.init()
if pygame.joystick.get_count() == 0:
    print("No joystick connected.")
    # quit()
else:
    js_connected= True
    print("Joystick Connected")
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
ls_x           = 0.0  
ls_y           = 0.0  
rs_x           = 0.0  
rs_y           = 0.0  
l_trig         = 0.0
r_trig         = 0.0 
a_btn          = 0.0
b_btn          = 0.0
x_btn          = 0.0
y_btn          = 0.0
l_bumper       = 0.0
r_bumper       = 0.0
hat_x          = 0.0 
hat_y          = 0.0 

# need this for 'sticky' joystick
js_offset= 0.2
#----------------------------------------------------//

#----------------GUI_init----------------------------\\
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("WSL --> ROS")
font = pygame.font.Font(None, 36)
text = ""
#----------------------------------------------------//

# while True:
while not rospy.is_shutdown():
    text= ''

    #-----------------------------Keyboard Input-------------------------------------\\
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            text= '  <<[A] '
            x_cnt-=0.7
            ls_x= -0.7
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            text= '    [D]>> '
            x_cnt+=0.7
            ls_x= 0.7
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            text= '     ^\n     ^\n    [W]        '
            ls_y= 0.7
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            text= '    [S]\n     v\n     v        '
            ls_y= -0.7
        elif keys[pygame.K_q]:
            print(x_cnt)
            quit()
        else: text = text[:-1]
        if event.type == pygame.KEYDOWN and text!= '':
            if keys[pygame.K_LEFT]:
                text= ("    ←")
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                text= ("    →")
            elif keys[pygame.K_UP] or keys[pygame.K_w]:
                text= ("    ↑")
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                text= ("    ↓")
            else: text += event.unicode
            if event.key == pygame.K_LSHIFT:
                if ls_x>0.0 : ls_x=1
                if ls_x<0.0 : ls_x=-1
                if ls_y>0.0 : ls_y=1
                if ls_y<0.0 : ls_y=-1
        #----------------------------------------------------------------------------//

    #----------------------------------------------------\----------------Joystick_cap----------------------\----------------------------------------------------\\
    if(js_connected):
        ls_x   = '%.3f'%(joystick.get_axis(0))
        ls_y   = '%.3f'%(joystick.get_axis(1))
        rs_x   = '%.3f'%(joystick.get_axis(2))
        rs_y   = '%.3f'%(joystick.get_axis(3))
        l_trig = '%.3f'%(joystick.get_axis(4))
        r_trig = '%.3f'%(joystick.get_axis(5))
        a_btn  = joystick.get_btn(0)
        b_btn  = joystick.get_btn(1)
        x_btn  = joystick.get_btn(2)
        y_btn  = joystick.get_btn(3)
        l_bumpe= joystick.get_btn(4)
        r_bumpe= joystick.get_btn(5)
        hat_x  = joystick.get_hat(0)[0]
        hat_y  = joystick.get_hat(0)[1]
        if(float(ls_x)<(0.000-js_offset)): 
            text= ("     <<[LS]")
            x_cnt-=1
        if(float(ls_x)>(0.000+js_offset)): 
            text= ("    [LS]>>")
            x_cnt+=1
        if(float(ls_y)<(0.000-js_offset)): 
            text= '    [LS]\n     v\n     v        '
            x_cnt-=1
        if(float(ls_y)>(0.000+js_offset)): 
            text= '     ^\n     ^\n    [LS]'
            x_cnt+=1
        # if(float(rs_x)<0.000): 
        #     text= ("     <<[RS]")
        #     print( rs_x)
        # if(float(rs_x)>0.000): text= ("    [RS]>>")
    #----------------------------------------------------/----------------------------------------------------/----------------------------------------------------//


    #--------------- Display ---------------------------------------------------------\\
    if text!= '':
    #[+]-- '#####' first digit to select motor, last 4 motors is pwm from 1500-1750
        print(text)
        # print(x_cnt)
        print(ls_x)
        textRender = font.render(text, True, (255, 255, 255))
        text_rect = textRender.get_rect()
        text_rect.center = screen.get_rect().center
        screen.blit(textRender, text_rect)
    else: 
        screen.fill((0, 0, 0))
        ls_x= 0.0
        ls_y= 0.0
    pygame.display.update()
    #--------------- Display ---------------------------------------------------------//


    #----------------------------Publishinng-----------------------------\\
    # ser = serial.Serial('COM3', 9600) # Replace 'COM3' with the port your Teensy is connected to.
    # ser.write(b'Hello, Teensy!')
    # vel_msg = Twist() 
    vel_msg.linear.y = ls_y  # meters per second
    vel_msg.angular.z = ls_x  # radians per second 
    total = (
        vel_msg.linear.x + vel_msg.linear.y + vel_msg.linear.z +
        vel_msg.angular.x + vel_msg.angular.y + vel_msg.angular.z
    )
    if total!=0.0 and total!= -0.0:print((vel_msg))
    vel_publisher.publish(vel_msg)


    thrust_pwm= int(ls_y*Max_pwm)
    thrust_publisher.publish(thrust_pwm)
    if thrust_pwm!= 0.0: print('thrust_pwm -> /yaw_pwm',thrust_pwm)
    thurst_pwm= 0.0

    yaw_pwm= int(ls_x*Max_pwm)
    angVel_publisher.publish(yaw_pwm)
    if yaw_pwm!= 0.0: print('yaw_pwm -> /yaw_pwm_feedback',yaw_pwm)
    yaw_pwm= 0.0



    #[+]----------------------------------------------------
# Joystick.MAX_YAW_PWM_FEEDBACK = 1750
# def input_rotate(self, joy_input):
#     # the input will be a value between -1 and 1, which maps nicely to manual control of a max yaw PWM
#     yaw_pwm = int(joy_input * Joystick.MAX_YAW_PWM_FEEDBACK)
#     self.publish(Topics.YAW_PWM_FEEDBACK, yaw_pwm)
#     print("Set yaw PWM to " + str(yaw_pwm))
#--------------------------------------------------------
    # angVel_msg.publish(<target angle>)

    #--------------------------------------------------------------------//

    rospy.sleep(0.25)
    # pygame.time.wait(200)


