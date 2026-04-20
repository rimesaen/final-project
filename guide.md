# A COMPREHENSIVE GUIDE TO SURVIVAL

Last Update: 4 April 2026

> Recommendation: listen to some Soulsborne boss OST while going through this guide. It's about to be lore accurate.

## Table of Contents
1. [Setting up the virtual machine](#setting-up-the-virtual-machine)
2. [Setting up the simulation](#setting-up-the-simulation)

    - [Testing out the simulation (manual control)](#testing-out-the-simulation-manual-control)
    - [Testing out the simulation (wall-following)](#testing-out-the-simulation-wall-following)
    - [Testing out the real world (manual control)](#testing-out-the-real-world-manual-control)
    - [Testing out the real world (wall-following)](#testing-out-the-real-world-wall-following)
    - [Taking pictures + wall following (in simulation)](#taking-pictures--wall-following-in-simulation)

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

4. Install some more stuff.

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

### Testing out the manual control (simulation)

> UNTESTED AS OF APRIL

1. First terminal:

```
source /opt/ros/humble/setup.bash
source ~/final-project/crazyflie_mapping_demo/ros2_ws/install/setup.bash
export GZ_SIM_RESOURCE_PATH=~/final-project/crazyflie_mapping_demo/ros2_ws/src/cf-gz/ros_gz_crazyflie_gazebo/models
export LIBGL_ALWAYS_SOFTWARE=1
ros2 launch crazyflie_ros2_multiranger_bringup simple_mapper_simulation.launch.py
```

2. Second terminal:

```
source /opt/ros/humble/setup.bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

### Testing out the wall-following (simulation)

#### Single drone without camera

1. Only terminal:
```
source /opt/ros/humble/setup.bash
source ~/final-project/crazyflie_mapping_demo/ros2_ws/install/setup.bash
export GZ_SIM_RESOURCE_PATH=~/final-project/crazyflie_mapping_demo/ros2_ws/src/cf-gz/ros_gz_crazyflie_gazebo/models
export LIBGL_ALWAYS_SOFTWARE=1
ros2 launch crazyflie_ros2_multiranger_bringup wall_follower_mapper_single_simulation.launch.py
```

#### Single drone with camera

> Finally, we give the drone *eyes* in simulation. Whether it sees the truth or just more bugs… remains to be seen.

1. First terminal: 

```
source /opt/ros/humble/setup.bash
source ~/final-project/crazyflie_mapping_demo/ros2_ws/install/setup.bash
export GZ_SIM_RESOURCE_PATH=~/final-project/crazyflie_mapping_demo/ros2_ws/src/cf-gz/ros_gz_crazyflie_gazebo/models
export LIBGL_ALWAYS_SOFTWARE=1
ros2 launch crazyflie_ros2_multiranger_bringup wall_follower_mapper_single_camera_simulation.launch.py
```

2. Second terminal: 

```
source /opt/ros/humble/setup.bash
rqt_image_view /crazyflie/camera
```

> The camera topic is bridged automatically

> The images are saved in ros2_ws in a folder named **wall_follower_images**

I take it worked by the look on your face ^^

#### Double drones without camera

1. Only terminal:

```
source /opt/ros/humble/setup.bash
source ~/final-project/crazyflie_mapping_demo/ros2_ws/install/setup.bash
export GZ_SIM_RESOURCE_PATH=~/final-project/crazyflie_mapping_demo/ros2_ws/src/cf-gz/ros_gz_crazyflie_gazebo/models
export LIBGL_ALWAYS_SOFTWARE=1
ros2 launch crazyflie_ros2_multiranger_bringup wall_follower_mapper_double_simulation.launch.py
```

#### Double drones with camera

1. First terminal: 

```
source /opt/ros/humble/setup.bash
source ~/final-project/crazyflie_mapping_demo/ros2_ws/install/setup.bash
export GZ_SIM_RESOURCE_PATH=~/final-project/crazyflie_mapping_demo/ros2_ws/src/cf-gz/ros_gz_crazyflie_gazebo/models
export LIBGL_ALWAYS_SOFTWARE=1
ros2 launch crazyflie_ros2_multiranger_bringup wall_follower_mapper_double_camera_simulation.launch.py
```

2. Second terminal: 

```
source /opt/ros/humble/setup.bash
rqt
```

Inside RQT:

Go to: Plugins → Visualization → Image View
Select Topic: /{robot_prefix}/camera

> The images are saved in ros2_ws in a folder named **wall_follower_images/{robot_prefix}**

#### Quadruple drones with camera

1. First terminal: 

```
source /opt/ros/humble/setup.bash
source ~/final-project/crazyflie_mapping_demo/ros2_ws/install/setup.bash
export GZ_SIM_RESOURCE_PATH=~/final-project/crazyflie_mapping_demo/ros2_ws/src/cf-gz/ros_gz_crazyflie_gazebo/models
export LIBGL_ALWAYS_SOFTWARE=1
ros2 launch crazyflie_ros2_multiranger_bringup wall_follower_mapper_quadruple_camera_simulation.launch.py
```

2. Second terminal: 

```
source /opt/ros/humble/setup.bash
rqt
```

Inside RQT:

Go to: Plugins → Visualization → Image View
Select Topic: /{robot_prefix}/camera

> The images are saved in ros2_ws in a folder named **wall_follower_images/{robot_prefix}**

### Testing out the real world (manual control)

> UNTESTED AS OF APRIL

1. First terminal:

```
source /opt/ros/humble/setup.bash
source ~/final-project/crazyflie_mapping_demo/ros2_ws/install/setup.bash
export GZ_SIM_RESOURCE_PATH=~/final-project/crazyflie_mapping_demo/simulation_ws/cf-simulation/simulator_files/gazebo
ros2 launch crazyflie_ros2_multiranger_bringup simple_mapper_real.launch.py
```

2. Second terminal:

```
source /opt/ros/humble/setup.bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

### Testing out the real world (wall-following)

> UNTESTED AS OF APRIL

1. First terminal:

```
source /opt/ros/humble/setup.bash
source ~/final-project/crazyflie_mapping_demo/ros2_ws/install/setup.bash
export GZ_SIM_RESOURCE_PATH=~/final-project/crazyflie_mapping_demo/simulation_ws/cf-simulation/simulator_files/gazebo
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

> Due to rational fears of the future (i.e. cfclient has a conflict with OpenCV), cfclient should be installed on a virtual environment.

1. Create the virtual environment. From the project's root directory,

> To deactivate, simply run `deactivate`.

```
python3 -m venv client-venv
source client-venv/bin/activate
```

2. Everything should already be installed, but just in case, run:

```
cd cf-client
pip install -e .[dev]
```

3. To open cfclient, stay within the cf-client directory and run:

```
cfclient
```

### Crazyflie firmware

> The setup of the firmware (specifically for the AI deck) follows these guides [1](https://www.bitcraze.io/documentation/tutorials/getting-started-with-aideck/#flash-wifi-example) [2](https://www.bitcraze.io/documentation/repository/crazyflie-firmware/master/building-and-flashing/build/). The AI deck hasn't worked yet, so follow with caution!!

1. Ensure that the AI deck is the only deck connected.

2. In cfclient, flash the newest firmware. Writing to the AI deck should be mentioned in the progress.

    - If it works, you should see `ESP32: I (910) SYS: Initialized` in the console of cfclient when the drone is connected to (the console can be opened from *View*).

#### Wi-Fi connection & camera in real life

> WORKED!!!

1. Put your VMware in Bridge mode following this tutorial : https://youtu.be/7T4DYrosAfw?si=pRIoc5VGfkOzwLJT 

    - Remeber your "Bridge to" sellection in Virtual Network Editor (Personally I chose Intel(R) Wi-Fi 6 AX201 160MHz)
 
2. On the host pc, open Device Manager, then navigate to Network Adapters, and select your network sellection in step 1. Navigate to Advanced and set the value to 6.Dual Band 802. 11a/b/g.

    - Property should already be set to 802. 11a/b/g Wireless Mode.
    
3. Activate the client virtual environment as it is needed for *make cload* in later steps: 

```
source client-venv/bin/activate
```

4. Navigate to crazyflie-firmware and throw out the following commands:

    - The make distclean is to clean out previous configuration files, just in case.

```
make distclean
make cf2_defconfig
```

5. Change configurations by going into menu config.

```
make menuconfig
```

    - Go to Expantion Deck Configuration > Deck Drivers and check Support the AI Deck
    
    - beneath Support the AI Deck set Wifi Setup and Startup to Access point (AP) mode
    
    - *IMPORTANT* Please DO change the SSID and Password (if you don't the network will not show up)

6. Once done,

    - During `make cload`, press and hold the power button of the drone for 3 seconds to enter bootloader mode.

```
make -j$(nproc)
make cload
```

7. Now in you host computer connect to "WiFi streaming example" in the list of you available netwroks.

    - *The drone must be in bootloader mode for you to see the network listed* 

    - Your WMware automatically should be connected to the same network if the bridge mode is set correctly. To check, inside a terminal in your WMware run:

```
sudo dhclient -v ens33
```
    - You should see : DHCPACK of 192.168.4.3 from 192.168.4.1
    
> Wi-Fi name does not show up?! SOLVED

If the wifi does not show up in your list of available networks in the host pc follow *Flash Wifi Example* in [1](https://www.bitcraze.io/documentation/tutorials/getting-started-with-aideck/#flash-wifi-example). After downloading the required file the commad will be: 

```
cfloader flash aideck_gap8_wifi_img_streamer_with_ap.bin deck-bcAI:gap8-fw -w radio://0/80/2M/E7E7E7E7E7
```

YAY!


8. Activate the following virtual environment with openCV installed.

```
source opencv-venv/bin/activate
```
    
9. To test the camera run :

    - Make sure the drone is at least 80cm away from the pc you're running the command in or the signal would be too loud and you may get black camera feed.

```
cd ~/final-project/aideck-gap8-examples/examples/other/wifi-img-streamer
python3 opencv-viewer.py -n 192.168.4.1
```
> Scrip doen't run / stopped running!! SOLVED

If for any reason the script does not run, it is most probably a wifi connection issue so *first turn the drone on and off* and then try the following:

Inside WMware run:

```
ip a
```
you should see *inet 192.168.4.1*. If not reconnect to WiFi streaming example in the host pc and run the following in WMware :

```
sudo dhclient
```

To check if you're acctually connected, run the following:

```
ping 192.168.4.1
```

you should see *64 bytes from 192.168.4.1*

VOLA!!

## Troubleshooting

### The network has run away!

Throw the command `sudo dhclient` into the terminal and pray the network comes back. 99% possibility that you will have to do this everytime you start the VM up.

- There possibly exists a fix out there related to netplan, but alas, it is but a myth.

### Doctor, quick! The patient is unresponsive!

Try starting the drone up in bootloader mode (press and hold power button for 3 seconds) and doing a cold boot on cfclient.

### GitHub wants authentication but it's not letting me in!

Use `gh auth login` instead of whatever they're suggesting. Unless they're suggesting `gh auth login`, in which case, do that.

### Colcon build? More like colcon... doesn't build...

Pull a quick little

```
cd ~/final-project/crazyflie_mapping_demo/ros2_ws
rm -rf build/ install/ log/ wall_follower_images/
cd ~/final-project/crazyflie_mapping_demo/ros2_ws
source /opt/ros/humble/setup.bash
colcon build --cmake-args -DBUILD_TESTING=ON
```

### Rvis Global Status is ERROR!!

First, check your Gazebo version and make sure you have the right one. But if you have the right one and it doesn't work...

Don't panic! On the top of this guide and under "Setting up the simulation" and then "Procedure" run steps 4 and 5 again. It'll work, promise ;)

### Rvis map loads wierdly and drone acts irregularly!!!

That may be because of Rvis not closing properly last time and hence run the following:

```
pkill -9 rviz
pkill -9 rviz2
```

