# ROS Setup Instructions + Python Pub Sub 
>⚡**It is HIGHLY suggested, to watch the first 4-5 videos in [this ROS YouTube tutorial playlist](https://www.youtube.com/playlist?list=PLAjUtIp46jDcQb-MgFLpGqskm9iB5xfoP) if you are not familiar with ROS basic concepts⚡**

## Installing Ubuntu Focal Fossa on a VM
1. Download Ubuntu Focal Fossa from [here](https://releases.ubuntu.com/20.04/)
2. Install Ubuntu on a Virtual Machine ([guide in italian for Virtual Box](https://www.youtube.com/watch?v=62-hJarauK4&list=PLhlcRDRHVUzR-5TKDC1VPMtyhEyyQ5uwy)).
Allocate at least 25 GB of disk space and install with the minimal installation option.
3. Update Ubuntu `sudo apt-get update && sudo apt-get upgrade`.
4. Tweak VM settings to [improve performances](http://www.rawinfopages.com/tips/2017/07/speed-up-virtualbox-in-windows/).

## Installing ROS 1 Noetic
### 1. Configure Ubuntu repo
Configure your Ubuntu repositories to allow "restricted," "universe," and "multiverse."
The simplest way to do it is go on the Software and Updates app in the menù, and search and check the options that contain the words restricted, multiverse and universe. 
You can follow the [Ubuntu guide for instructions on doing this](https://help.ubuntu.com/community/Repositories/Ubuntu).

Open a terminal and imput those commands:
    
    sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

### 2. Set up keys
    sudo apt install curl # if you haven't already installed curl
    curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
### 3. Installation of the full version of ROS Noetic (recommended)
    sudo apt update
    sudo apt install ros-noetic-desktop-full
### 4. Env. Setup
    echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
    source ~/.bashrc
This will ensure that every time you open a shell the command `source /opt/ros/noetic/setup.bash` is executed automatically.
### 5. Install dependencies for building packages
    sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
    
    #initialize rosdep
    sudo rosdep init
    rosdep update

    #install catkin
    sudo apt install python3-catkin-tools python3-osrf-pycommon

Refer to [this guide](http://wiki.ros.org/noetic/Installation/Ubuntu) for additional info.
Also thsi [video tutorial for ROS installation](https://youtu.be/PowY8dV36DY).


## Useful Links
- [ROS Wiki](http://wiki.ros.org/Documentation)
- [ROS Beginner Python Tutorial (YT Playlist)](https://www.youtube.com/playlist?list=PLAjUtIp46jDcQb-MgFLpGqskm9iB5xfoP)
- [Project example + video tutorial](https://github.com/utra-robosoccer/Tutorials-2020)

