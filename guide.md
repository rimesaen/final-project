# A COMPREHENSIVE GUIDE TO SURVIVAL

Last Update: 6 February 2026

> Recommendation: listen to some Soulsborne boss OST while going through this guide. It's about to be lore accurate.

## Table of Contents
1. [Setting up the virtual machine](#setting-up-the-virtual-machine)
2. [Setting up the simulation](#setting-up-the-simulation)

    - [Testing out the simulation (manual control)](#testing-out-the-simulation-manual-control)
    - [Testing out the simulation (wall-following)](#testing-out-the-simulation-wall-following)
    - [Testing out the real world (manual control)](#testing-out-the-real-world-manual-control)
    - [Testing out the real world (wall-following)](#testing-out-the-real-world-wall-following)

3. [Setting up the drones](#setting-up-the-drones)

    - [Drones assembly](#drones-assembly)
    - [Crazyradio](#crazyradio)
    - [Crazyflie client](#crazyflie-client)
    - [Crazyflie firmware](#crazyflie-firmware)
    - [Wi-Fi connection](#wi-fi-connection)

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

### Testing out the simulation (manual control)

1. First terminal:

```
source /opt/ros/humble/setup.bash
source ~/final-project/crazyflie_mapping_demo/ros2_ws/install/setup.bash
export GZ_SIM_RESOURCE_PATH=~/final-project/crazyflie_mapping_demo/simulation_ws/crazyflie-simulation/simulator_files/gazebo
export LIBGL_ALWAYS_SOFTWARE=1
ros2 launch crazyflie_ros2_multiranger_bringup simple_mapper_simulation.launch.py
```

2. Second terminal:

```
source /opt/ros/humble/setup.bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

### Testing out the simulation (wall-following)

> Worked previously, but now doesn't... Will also be updating with improvements to the algorithm.

1. First terminal:

```
source /opt/ros/humble/setup.bash
source ~/final-project/crazyflie_mapping_demo/ros2_ws/install/setup.bash
export GZ_SIM_RESOURCE_PATH=~/final-project/crazyflie_mapping_demo/simulation_ws/crazyflie-simulation/simulator_files/gazebo
export LIBGL_ALWAYS_SOFTWARE=1
ros2 launch crazyflie_ros2_multiranger_bringup wall_follower_mapper_simulation.launch.py
```

2. To stop the drone:

```
source /opt/ros/humble/setup.bash
ros2 service call /crazyflie/stop_wall_following std_srvs/srv/Trigger
```

### Testing out the real world (manual control)

> Not yet tested!

1. First terminal:

```
source /opt/ros/humble/setup.bash
source ~/final-project/crazyflie_mapping_demo/ros2_ws/install/setup.bash
export GZ_SIM_RESOURCE_PATH=~/final-project/crazyflie_mapping_demo/simulation_ws/crazyflie-simulation/simulator_files/gazebo
ros2 launch crazyflie_ros2_multiranger_bringup simple_mapper_real.launch.py
```

2. Second terminal:

```
source /opt/ros/humble/setup.bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

### Testing out the real world (wall-following)

> Not yet tested!

1. First terminal:

```
source /opt/ros/humble/setup.bash
source ~/final-project/crazyflie_mapping_demo/ros2_ws/install/setup.bash
export GZ_SIM_RESOURCE_PATH=~/final-project/crazyflie_mapping_demo/simulation_ws/crazyflie-simulation/simulator_files/gazebo
ros2 launch crazyflie_ros2_multiranger_bringup wall_follower_mapper_real.launch.py
```

2. To stop the drone:

```
source /opt/ros/humble/setup.bash
ros2 service call /crazyflie/stop_wall_following std_srvs/srv/Trigger
```

## Setting up the drones

### Drones assembly

> The guide to assembling the drones can be found [here](https://www.bitcraze.io/documentation/tutorials/getting-started-with-crazyflie-2-x/).

### Crazyradio

> The guide to connecting the Crazyradio can be found [here](https://www.bitcraze.io/documentation/tutorials/getting-started-with-crazyradio-2-0/). There shouldn't be a need to flash new firmware if the Crazyradio has been flashed recently before.

### Crazyflie client

> The setup of cfclient follows this [guide](https://www.bitcraze.io/documentation/repository/crazyflie-clients-python/master/installation/install/) from bitcraze.

1. From the final-project directory,

```
cd cf-client
pip install -e .[dev]
```

2. To open cfclient, stay within the cf-client directory and run:

```
cfclient
```

### Crazyflie firmware

> The setup of the firmware (specifically for the AI deck) follows these guides [1](https://www.bitcraze.io/documentation/tutorials/getting-started-with-aideck/#flash-wifi-example) [2](https://www.bitcraze.io/documentation/repository/crazyflie-firmware/master/building-and-flashing/build/). The AI deck hasn't worked yet, so follow with caution!!

1. Ensure that the AI deck is the only deck connected.

2. In cfclient, flash the newest firmware. Writing to the AI deck should be mentioned in the progress.

    - If it works, you should see `ESP32: I (910) SYS: Initialized` in the console of cfclient when the drone is connected to (the console can be opened from *View*).

#### Wi-Fi connection

> NOT WORKING!!! I REPEAT, NOT WORKING!!!!!!

1. Navigate to crazyflie-firmware and throw out the following commands:

    - The make distclean is to clean out previous configuration files, just in case.

```
make distclean
make cf2_defconfig
```

2. Change configurations by going into menu config.

```
make menuconfig
```

3. Once done,

    - During `make cload`, press and hold the power button of the drone for 3 seconds to enter bootloader mode.

```
make -j$(nproc)
make cload
```

## Troubleshooting

### The network has run away!

Throw the command `sudo dhclient` into the terminal and pray the network comes back. 99% possibility that you will have to do this everytime you start the VM up.

- There possibly exists a fix out there related to netplan, but alas, it is but a myth.

### Doctor, quick! The patient is unresponsive!

Try starting the drone up in bootloader mode (press and hold power button for 3 seconds) and doing a cold boot on cfclient.
