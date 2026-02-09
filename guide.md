# A COMPREHENSIVE GUIDE TO SURVIVAL

Last Update: 6 February 2026

> Recommendation: listen to some Soulsborne boss OST while going through this guide. It's about to be lore accurate.

## Table of Contents
1. [Setting up the virtual machine](#setting-up-the-virtual-machine)
2. [Setting up the simulation](#setting-up-the-simulation)
3. [Setting up the drones](#setting-up-the-drones)

- [Errors! Errors galore!](#troubleshooting)

## Setting up the virtual machine

### Context

> - Virtual Machine: *VMWare Workstation 17 Pro*
> - Operating System: *Ubuntu 64-bit, 22.04.5 LTS*
> - Hard Disk: *80 GB (tentative)*
> - Memory: *8000 MB (tentative)*
> - Network connection: *NAT*

### Procedure

1. Install [VMWare Workstation](https://www.vmware.com/products/desktop-hypervisor/workstation-and-fusion).

2. Get the [Ubuntu ISO file](https://ubuntu.com/download/desktop).

3. Run through the VM installation.

    - Ensure sufficient hard disk size!! If too little, there may be problems later on.

4. Set up Git (for the sake of cloning this repository).
  
5. Clone this repository!

## Setting up the simulation

### Context

> The setup of ROS 2 and Gazebo partially follows this [guide](https://www.bitcraze.io/2024/09/crazyflies-adventures-with-ros-2-and-gazebo/) from bitcraze, but there is no need to go there, for this guide is totally comprehensive. (not)
> - ROS 2 Humble
> - Gazebo Harmonic

### Procedure

1. Install ROS 2 Humble, following this [guide](https://docs.ros.org/en/rolling/Installation/Ubuntu-Install-Debs.html).

    - Do the recommended desktop install as well as the development tools. No idea what dev tools do but hey, free stuff.
    - This will take a long while. Read a few angsty books and be happy that you're dealing with *this* and not *that*.
  
2. Install Gazebo Harmonic, following this [guide](https://gazebosim.org/docs/harmonic/install_ubuntu/).

    - Hope you haven't finished all your books by this point.
  
3. Clone this repository.

```
git clone https://github.com/rimesaen/final-project.git --recursive
```

5. Install some more stuff.

```
sudo apt-get install libboost-program-options-dev libusb-1.0-0-dev python3-colcon-common-extensions
sudo apt-get install ros-humble-motion-capture-tracking ros-humble-tf-transformations
sudo apt-get install ros-humble-ros-gzharmonic ros-humble-teleop-twist-keyboard
pip3 install cflib transform3D
```

5. Build the packages.

    - Pay attention to the directory! It might change according to where you've placed the repository!

```
cd ~/final-project/crazyflie_mapping_demo/ros2_ws
source /opt/ros/humble/setup.bash
colcon build --cmake-args -DBUILD_TESTING=ON
```

6. Voila! That should work! Hopefully!

### Testing out the simulation (simple mapping, manually controlled)

1. First terminal:

```
source ~/final-project/crazyflie_mapping_demo/ros2_ws/install/setup.bash
export GZ_SIM_RESOURCE_PATH=~/final-project/crazyflie_mapping_demo/simulation_ws/crazyflie-simulation/simulator_files/gazebo
export LIBGL_ALWAYS_SOFTWARE=1
ros2 launch crazyflie_ros2_multiranger_bringup simple_mapper_simulation.launch.py
```

2. Second terminal:

```
source ~/final-project/crazyflie_mapping_demo/ros2_ws/install/setup.bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

3. Voila x2! That oughta work!

## Setting up the drones

TBA, for I am but a poor and humble farmer with naught the will to live.

## Troubleshooting

### The network has run away!

Throw the command `sudo dhclient` into the terminal and pray the network comes back. 99% possibility that you will have to do this everytime you start the VM up.

- There possibly exists a fix out there related to netplan, but alas, it is but a myth.

### 
