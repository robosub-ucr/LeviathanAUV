# Automation Onboarding Task

>**Created:** 10/23/2023
>
>**Updated:** 10/23/2023
>
>**Author:** Joshua Shabun
>

**Relevancies:** Linux, Python, ROS, Gazebo, Automation, Onboarding

> ***This onboarding task/automation tutorial was adapted from UCR EE144 Lab 1: [Link](https://ucr-ee144.readthedocs.io/en/latest/lab1.html)***

## 1. Requirements
- [ ] Ubuntu 18.04 - 18.04.6
- [ ] ROS Melodic (refer to documentation for help)
- [ ] Gazebo (refer to documentation for help)

## 2. Creating another catkin workspace

**vm password:** robosub2024

In order to complete this onboarding task, we need to create a separate catkin workspace that does not conflict with our main robosub workspace. Please follow the steps below carefully in order to complete this step.
1. Open a new terminal window and make sure you're in the home directory.
2. Create a new catkin directory
```bash
mkdir -p ~/robosub_automation/onboarding_catkin_ws/src
cd ~/robosub_automation/onboarding_catkin_ws/
catkin_make
```
3. Add the new workspace to your `.bashrc`.
  * `cd` into your home directory
  * `gedit .bashrc` should open up a text editor with your bash config file
  * Scroll to the bottom of the file and add the line `source ~/robosub_automation/onboarding_catkin_ws/devel/setup.bash`
  * Select save and close gedit
  * Run `source .bashrc` to reload terminal with the new updated config 
  * **IMPORTANT**: After demoing this task to one of the Software Leads, go back into your `.bashrc` and remove the source line you added or else the robosub workspace will not activate.

## 3. ROS Basics
1. `cd` into your new catkin workspace
2. Install the following dependencies
`sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential`
3. Initialize rosdep
```bash
sudo apt install python-rosdep
sudo rosdep init
rosdep update
```
4. Create a new ROS package
```bash
cd ~/robosob_automation/onboarding_catkin_ws/src
catkin_create_pkg onboardingf23 std_msgs rospy
```
5. There should now be a new package called `onboardingf23`
6. Build the package
```bash
cd ~/robosub_automation/onboarding_catkin_ws/
catkin_make
```

## 4. Set up Turtlebot in Gazebo
1. Upgrade packages and install Turtlebot dependencies
```bash
sudo apt-get update
sudo apt-get install sudo apt-get install ros-melodic-turtlebot3-*
sudo apt-get install ros-melodic-kobuki-ftdi ros-melodic-ar-track-alvar-msgs
```
2. Navigate to `onboardingf23` package and create a new folder and a new launch file
```bash
roscd onboardingf23
mkdir launch
cd launch
touch gazebo.launch
gedit gazebo.launch
```
3. Copy and paste the following script, then save it.
```
<launch>
  <arg name="world_file" default="worlds/empty.world"/>

  <arg name="urdf" default="$(find turtlebot_description)/robots/kobuki_hexagons_astra.urdf.xacro" />
  <param name="robot_description" command="$(find xacro)/xacro --inorder $(arg urdf)" />

  <!-- include two nodes gazebo (server) and gazebo_gui (client) -->
  <include file="$(find gazebo_ros)/launch/empty_world.launch">
    <arg name="world_name" value="$(arg world_file)"/>
  </include>

  <!-- Gazebo model spawner -->
  <node name="spawn_turtlebot_model" pkg="gazebo_ros" type="spawn_model"
        args="$(optenv ROBOT_INITIAL_POSE) -unpause -urdf -param robot_description -model mobile_base"/>

  <!-- Velocity muxer -->
  <node pkg="nodelet" type="nodelet" name="mobile_base_nodelet_manager" args="manager"/>
  <node pkg="nodelet" type="nodelet" name="cmd_vel_mux"
        args="load yocs_cmd_vel_mux/CmdVelMuxNodelet mobile_base_nodelet_manager">
    <param name="yaml_cfg_file" value="$(find turtlebot_bringup)/param/mux.yaml"/>
    <remap from="cmd_vel_mux/output" to="mobile_base/commands/velocity"/>
  </node>

  <!-- Publish robot state -->
  <node pkg="robot_state_publisher" type="robot_state_publisher" name="robot_state_publisher">
    <param name="publish_frequency" type="double" value="30.0" />
  </node>

</launch>
```
4. Add proper models to gazebo
```bash
git clone https://github.com/osrf/gazebo_models.git
mkdir -p ~/.gazebo/models
cp -r gazebo_mdoels/* ~/.gazebo/models
rm -rf gazebo_models
```
5. Rerun gazebo and models should appear

## 5. Run Turtlebot in Gazebo
1. Launch Gazebo and spawn a new robot by following the command. It may take a while the first time you open Gazebo since it will need to download some models and world environments.
```bash
export TURTLEBOT3_MODEL=burger
roslaunch onbaordingf23 gazebo.launch
```
2. Once the robot is successfully spawned in Gazebo, open a new terminal and launch the teleop node
```bash
roslaunch turtlebot_teleop keyboard_teleop.launch
```
3. Keep the teleop terminal open (selected) and you should be able to control the robot using keyboard now. The teleop program in this terminal takes in whatever keys you entered and converts them into velocity commands to send to the robot. Now spend some time playing with it! (Don’t send the keyboard teleop commands to the Gazebo window, it won’t work; send commands to the terminal)
4. You can also put some obstacles (objects) in Gazebo simulation environment, and drive the robot to collide with obstacles. See what happens :)
5. To terminate the programs running in terminal, use `ctrl + c` and wait for the programs to end.

## 6. Set up robot arm in Gazebo
1. Download ROS packages for the robot arm
```bash
cd ~/robosub_automation/onboarding_catkin_ws/src
git clone https://github.com/UCR-Robotics/interbotix_ros_arms.git
```
2. Install dependencies
```bash
cd ~/onboarding_catkin_ws
rosdep update
rosdep install --from-paths src --ignore-src -r -y
```
3. We need to add one more package that is not currently supported by rosdep installation
```bash
sudo apt install python-pip
sudo pip install modern_robotics
```
4. Build the ROS package
```bash
cd ~/onboarding_catkin_ws
catkin_make
```

## 7. Play with the robot arm in Gazebo
1. Launch the ReactorX 150 robot arm in Gazebo
```bash
roslaunch interbotix_moveit interbotix_moveit.launch robot_name:=rx150 use_gazebo:=true
```
2. You will see the robot arm is ready in Gazebo but the RViz (the visualization software used in ROS) is still pending. This is because it is still waiting for Gazebo to start simulation. In the bottom left of Gazebo window, you will see a small Play ▶ button. Click it to let it run!
3. Once Gazebo starts simulation, the RViz will prompt you two panels on the left and a visualization of the robot arm on the right. On the top left panel, go to “MotionPlanning” -> “Planning Request” -> “Query Goal State” and check this box. Then you can drag the “ball” on the tip of the robot arm to wherever you want it to go.
4. Once a goal pose is set, in the bottom left panel, go to “Planning” tab and try buttons “Plan”, “Execute”, or “Plan and Execute”. Cool! The software can figure out a path for the arm to follow and reach the exact goal pose you just set. Spend some time playing with it!
5. You can also take a look at Gazebo to see the current status of the robot arm. RViz provides a tool for better interaction, but only Gazebo shows the real physical status.
