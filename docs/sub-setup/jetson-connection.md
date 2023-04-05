# Connecting to the Jetson and Initializing ROS Nodes

>**Created:** 08/07/2019
>
>**Updated:** 04/05/2023
>
>**Author:** Edward Carrasco (reviewed by Jack Kolb)
>
>**Updated By:** Joshua Shabun

**Relevancies:** Networking, Linux, Jetson TX2 Developer Kit, PuTTY, Xming

## Quick Reference
| Jetson Ethernet IP Address | ucr@10.42.0.1 |
| ----------- | ------- |
| **Jetson Ethernet Port** | **22** |
| **Jetson Password** | **seadragon**
| **Old IP Address**| **nvidia@169.254.201.249** |

## Introduction
This tutorial will show you how to connect your personal computer to the Jetson TX2 Developer Kit (referred to as the Jetson). When connected, you will be able to access the Jetson's files, run programs, and do any other task. The Jetson is the main computer in the Seadragon AUV. It contains the software that controls the Seadragon AUV’s behavior and sensors with the help of ROS. Most likely, the main reason you will want to connect to the Jetson is to initialize ROS and other subsystems.

Before connecting to the Jetson via SSH:
1. Connect the Jetson to a power source.
2. Turn on the Jetson.
3. If using Ethernet, plug an Ethernet cable to the Jetson's Ethernet port and to your computer's port. If your computer only has a USB port, use an Ethernet-to-USB adapter.
4. If using Wi-Fi, you will be unable to find the device unless you connect it to a monitor and check what the IP address is. Alternatively you could make a program that outputs the IP address to an LCD display… The IP address will likely change with every reboot, so it is best not to rely on this method unless you have a monitor and mouse on hand.

### Why use PuTTY and Xming
By default, you can SSH on Linux, Mac, and Windows 10. Open a terminal and type:
```bash
ssh nvidia@169.254.201.249
Password: seadragon
```

The IP address can be obtained using ARP, available in Linux/Mac/Windows:

> With the ethernet connected, use “arp -a” in the terminal to see the connected devices. Several devices will show “dynamic” next to them, one of them is the IP address of the Jetson. Typically this IP address does not change much, if at all.

You should be able to connect to the Jetson and use it via the built in windows terminal. However, there are some GUIs that we are going to use that do not work via the terminal. For this reason, on Windows, we need to install Xming. Xming will allow us to draw these GUIs. To work with and configure Xming more easily, we use PuTTY.

### How to install and setup PuTTY and Xming
1. Download and install PuTTY from https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html
2. Download and install Xming from https://sourceforge.net/projects/xming/
3. Run Xming. You only need to do this once every time you turn on or restart your computer.
4. Open PuTTY.
5. In Session, for Host Name (or IP address): `ucr@10.42.0.1` and port `22`.
6. In Connection > SSH > X11,
    * Check **Enable X11 forwarding**
    * X display location: **localhost**
7. (Optional) In Window > Colours, you may want to set the Default Foreground to (0,0,0) and Default Background (255,255,255) to make the terminal more visible when using your computer outdoors.
8. (Optional) In Session, for Saved Sessions type a name (tip: use the Host Name) and click on **Save**.

![Putty Screenshot](docs/media/connection-img1.png)

## How to SSH into the Jetson
### PuTTY (Windows)
1. Check that Xming is running.
2. Open PuTTY.
3. If you have a saved session, select it and press **Load**. If you don’t, follow the configuration instructions above.
4. In Session, click on **Open**. This should open a terminal. If you get an error, see Troubleshooting SSH.
5. In the new terminal, type the password: `seadragon`. You should now have access to the Jetson computer.

### Terminal (MacOS & Linux)
1. Open Terminal
2. Type `ssh -X ucr@10.42.0.1`
3. When prompted for the password, enter the password: `seadragon`. (Nothing will show when typing the password).
4. Hit enter
    * If prompted to accept a certificate, type `yes` and hit enter
5. You should now be connected to the Jetson

## How to initialize ROS and the Jetson's connected devices
Once you have SSH’d into the Jetson, type the following commands:

| Command | Output |
|---|-------------------------------------------------------|
| `screen` | Starts a screen session.<br> <br>Any processes running in Screen will continue to run even if your computer and Jetson get disconnected. <br><br> If your computer will remain physically connected during the entire test, this command is not needed. <br><br> Learn more: [linuxize.com/post/how-to-use-linux-screen](linuxize.com/post/how-to-use-linux-screen) |
| `roscore &` | Runs the core ROS program |
| `chmod 666 /dev/ttyACM0` | Gives permission to use this device. <br>Most likely, this will be the **AHRS** sensor that is connected via USB to the Jetson. |
|`rosrun myahrs_driver myahrs_driver _port:=/dev/ttyACM0 &`| Runs the AHRS sensor |
|`chmod 666 /dev/ttyACM1`|Gives permission to use this device.<br>Most likely, this will be the **STM32** that is connected via USB to the Jetson.|
|`rosrun rosserial_python serial_node.py _port:=/dev/ttyACM1`|Runs the STM32 microcontroller|
|`roslaunch motor_controllers attitude_control.launch`|Starts the motor controller, and launches a GUI to control the thrusters, PID values, depth, and yaw. This GUI can be closed without consequence. Set Depth scales to 100<br><br>PID Values:<br> - Yaw p=.82 i=.8 d=.54<br> - Depth p=.45 i=.1 d=.26|
|`python3 <my_script.py>`|Runs a python script. <br><br>Replace `<script.py>` with any .py file in the current directory.<br><br>If this command gives you errors, you may need to replace python3 with python to use Python 2.x instead.|
|Press CTRL+A, then CTRL+D|**Warning**: Only do this if you used the screen command.<br>Detaches the screen from the terminal, so whatever you had running stays running.|
|`exit`||

If you used screen, after running all the commands in blue, you may disconnect the Ethernet cable and that will not stop the processes that were started via SSH. The processes will continue running. To stop the processes, you must plug the Ethernet cable and connect via SSH again. 

### How to reconnect and kill processes
After you have unplugged the Ethernet cable, you may want to reconnect to stop processes or do something else.

1. Plug the Ethernet cable onto the Seadragon AUV and your computer.
2. SSH into the Jetson.
3. Type: `screen -r`
    * If you only had one screen session active, that one will be reattached.
    * If you more than one, you will need to append the session ID to this command.

At this point, you should be in the desired screen session. You may kill any process by typing: `kill <PID>` where `PID` is the process ID. To find a process ID, type: `ps -a` to show the list of running processes.