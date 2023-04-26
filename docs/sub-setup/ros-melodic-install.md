# ROS Melodic Installation
0. Link to [Ubuntu 18.04](http://old-releases.ubuntu.com/releases/18.04.5/ubuntu-18.04-desktop-amd64.iso) ISO file.

1. Setup sources.list

    `sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'`

2. Setup your keys

    `sudo apt install curl`
    
    `curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -`

3. Install Aptitude

    `sudo apt update`

    `sudo apt-getinstall aptitude`

    1. enter `Y` and hit `enter`

4. Installing ROS

    `sudo aptitude install ros-melodic-desktop-full`

    1. You will be prompted with a long list of dependencies. The first time, it will keep the dependencies uninstalled. Enter `n`

    2. Keep selecting `n` until you get a shorter list of depencies that need to be removed/downgraded/upgraded. Then select `y`

    3. You may get the error `-o APT::Get::Fix-Missing=true`. Repeat the aptitude command to install missing dependencies until ROS successfully installs. 

    To Find availabe packages, use:

    `apt search ros-melodic`

5. Environment setup

    1. Add ROS environment ariables to bashrc

        `echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc`
    
        `source ~/.bashrc`

6. Dependencies for building packages

    1. Install ROS dependencies and packages

        `sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential`

    2. Initialize rosdep

        `sudo apt install python-rosdep`

    3. Continute intializing
    
        `sudo rodep init`
        
        `rosdep update`

    * Note: If you run into issues here, try using a different internet connection. 