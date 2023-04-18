# Leviathan Simulation (Gazebo) Environment Setup

## Installation Guide
1. Install ROS Melodic (Follow [ros-melodic-install](/docs/sub-setup/ros-melodic-install) file)
2. Install git
    
    `sudo apt install git`
3. Clone the [GitHub](https://github.com/robosub-ucr/LeviathanAUV) Repository

    `git clone https://github.com/robosub-ucr/LeviathanAUV`
4. Create a simlink for catkin_ws (~catkin_ws -> ~/LeviathanAUV/catkin_ws)

    `ln -s ~/LeviathanAUV/catkin_ws ~/catkin_ws`
5. In the [Simulations Folder](https://drive.google.com/drive/folders/19kHElDDrDg2vB-SCCIpL52dIEHC7Jh83?usp=share_link) of the Google Drive, there are a few zipped folders:
   
    1. Download `Gazebo_Objects.zip`, extract in `~/LeviathanAUV/catkin_ws/src/Simulations/`. This will make a folder Gazebo_Objects

    2. Download `uuv_simulator.zip`, extract it in `~/LeviathanAUV/catkin_ws/src/`. This will make a folder uuv_simulator

    3. Download `uuv_descriptions_leviathan`, extract it in `~/LeviathanAUV/catkin_ws/src/`. This will make a folder uuv_descriptions_leviathan

6. Add the following to your bashrc file. Open terminal and open the file to edit.
    
    `vim .bashrc` or `gedit .bashrc`

     Copy the following code to the bottom of the bashrc file:
     ```bash
    export ROS_HOSTNAME=>>>YOUR COMPUTER NAME<<<
    #export ROS_MASTER_URI=https://apollo:11311
    source /opt/ros/melodic/setup.bashupload_lev
    source /usr/share/gazebo-9/setup.sh
    source ~/LeviathanAUV/catkin_ws/devel/setup.bash

    # GAZEBO PATHS
    export GAZEBO_PREFIX=~/LeviathanAUV/catkin_ws/install
    export GAZEBO_RESOURCE_PATH=${GAZEBO_PREFIX}/share/gazebo-9.0:${GAZEBO_RESOURCE_PATH}
    export GAZEBO_MODEL_PATH=${GAZEBO_PREFIX}/share/gazebo-9.0/models:${GAZEBO_MODEL_PATH}
    export GAZEBO_PLUGIN_PATH=${GAZEBO_PREFIX}/lib:${GAZEBO_PREFIX}/lib/x86_64-linux-gnu:${ GAZEBO_PLUGIN_PATH}

    # USEFUL ALIASES
    alias sd='ssh -X ucr@seadragon'
    alias gz_lev='roslaunch uuv_gazebo_worlds robosub_world.launch'
    alias spawn_lev='roslaunch uuv_descriptions_leviathan upload_leviathan.launch mode:=default x:=0 y:=0 z:=-50 namespace:=leviathan'
    alias control_lev='roslaunch motor_controllers attitude_control.launch'
    alias sim_lev='python3 ~/LeviathanAUV/catkin_ws/src/Simulations/gazebo_link.py'
     ``` 
7. In the Simulations Google Drive folder there is a folder `RoboSub Gazebo World` and files `robosub_world.launch` and `robosub_world.world`

    1. Download and place the `robosub_world.world` into `~/LeviathanAUV/catkin_ws/src/uuv_simulator/uuv_gazebo_worlds/worlds`

    2. Download and place `robosub_world.launch` into `~/LeviathanAUV/catkin_ws/src/uuv_simulator/uuv_gazebo_worlds/launch`

8. Compile catkin_ws. Open terminal and type:

    `cd ~/catkin_ws`

    `catkin_make`

9. Install some ROS packages for Gazebo
    
    `cd ~/catkin_ws`

    `sudo apt-get install python-rosdep2`

    `sudo rosdep init`

    `rosdep update`

    `rosdep install --from-paths src --ignore-src --rosdistro=melodic -y --skip-keys "gazebo gazebo_msgs gazebo_plugins gazebo_ros gazebo_ros_control gazebo_ros_pkgs"`

    `sudo apt-get install ros-melodic-gazebo-ros-pkgs ros-melodic-gazebo-ros-control ros-melodic-pid ros-melodic-rqt-graph python3-pip rosbash ros-melodic-dynamic-reconfigure ros-melodic-rqt-reconfigure ros-melodic-xacro`

    `sudo pip3 install rospkg`

    `catkin_make install`

10. Copy the environment model folders from:
    `~/LeviathanAUV/catkin_ws/src/Simulations/Gazebo_Objects` to `~/LeviathanAUV/catkin_ws/src/uuv_simulator/uuv_gazebo_world/models`

11. To launch the simulations: (you will need multiple terminal windows/tabs)
    * **Terminal 1**: `roscore`
    * **Terminal 2**: `gz_lev`
    * **Terminal 3**: `spawn_lev`
    * **Terminal 4**: `python ~/LeviathanAUV/catkin_ws/src/Simulations/gazebo_link.py`
    * **Terminal 5**: `control_lev`

12. **Optional**: Install terminator to make launching ROS easier
    `sudo apt-get install terminator`

    There is now a terminator app installed on your ubuntu machine to use in place of the default terminal. You can right click anywhere in terminator to split horizontally and vertically to make running multiple terminal windows easier. 

## Common and Resolved Issues
When you add a model to the simulation, you might see it show up on Gazebo but not on the ROS camera. This is because the ROS camera pulls files from Gazebo’s internal path, not paths that we add using the “Add Path” button. If you go to Gazebo’s “Insert” tab, one of the paths should be in your `/home/{user}/catkin_ws` directory, such as `“/home/{user}/catkin_ws/src/uuv_simulator/uuv_gazebo_worlds/models”`. That is the easiest place to place models since it’s in catkin, so just copy/paste the model folder into there and it will show up. Drag the model into Gazebo, and it will show up both in Gazebo and on the ROS camera.
