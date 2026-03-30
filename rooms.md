## Table of Contents

1. [4x4 room](#4x4-room)
2. [L-shaped room](#l-shaped-room)

## 4x4 room

```
<?xml version="1.0" ?>

<sdf version="1.8">
  <world name="demo">
    <plugin
      filename="gz-sim-physics-system"
      name="gz::sim::systems::Physics">
    </plugin>
    <plugin
      filename="gz-sim-sensors-system"
      name="gz::sim::systems::Sensors">
      <render_engine>ogre2</render_engine>
    </plugin>
    <plugin
      filename="gz-sim-scene-broadcaster-system"
      name="gz::sim::systems::SceneBroadcaster">
    </plugin>
    <plugin
      filename="gz-sim-user-commands-system"
      name="gz::sim::systems::UserCommands">
    </plugin>

    <light name="sun" type="directional">
      <cast_shadows>true</cast_shadows>
      <pose>0 0 10 0 0 0</pose>
      <diffuse>0.8 0.8 0.8 1</diffuse>
      <specular>0.2 0.2 0.2 1</specular>
      <attenuation>
        <range>1000</range>
        <constant>0.9</constant>
        <linear>0.01</linear>
        <quadratic>0.001</quadratic>
      </attenuation>
      <direction>-0.5 0.1 -0.9</direction>
    </light>

    <model name="ground_plane">
      <static>true</static>
      <link name="link">
        <collision name="collision">
          <geometry>
            <plane>
              <normal>0 0 1</normal>
              <size>100 100</size>
            </plane>
          </geometry>
        </collision>
        <visual name="visual">
          <geometry>
            <plane>
              <normal>0 0 1</normal>
              <size>100 100</size>
            </plane>
          </geometry>
          <material>
            <ambient>0.8 0.8 0.8 1</ambient>
            <diffuse>0.8 0.8 0.8 1</diffuse>
            <specular>0.8 0.8 0.8 1</specular>
          </material>
        </visual>
      </link>
    </model>
    <include>
      <uri>model://crazyflie</uri>
      <name>crazyflie</name>
      <pose>0.0 0.0 0 0 0 -1.57</pose>
    </include>

    <model name="wall1">
      <pose>2 0 0.5 0 0 0</pose>
      <static>true</static>
      <link name="link">
        <visual name="visual">
          <geometry>
            <box>
              <size>0.2 4 2</size>
            </box>
          </geometry>
        </visual>
      </link>
    </model>

    <model name="wall2">
      <pose>-2 0 0.5 0 0 0</pose>
      <static>true</static>
      <link name="link">
        <visual name="visual">
          <geometry>
            <box>
              <size>0.2 4 2</size>
            </box>
          </geometry>
        </visual>
      </link>
    </model>

    <model name="wall3">
      <pose>0 2 0.5 0 0 1.57</pose>
      <static>true</static>
      <link name="link">
        <visual name="visual">
          <geometry>
            <box>
              <size>0.2 4 2</size>
            </box>
          </geometry>
        </visual>
      </link>
    </model>

    <model name="wall4">
      <pose>0 -2 0.5 0 0 1.57</pose>
      <static>true</static>
      <link name="link">
        <visual name="visual">
          <geometry>
            <box>
              <size>0.2 4 2</size>
            </box>
          </geometry>
        </visual>
      </link>
    </model>
  </world>
</sdf>
```

## L-shaped room

```
<?xml version="1.0" ?>

<sdf version="1.8">
  <world name="demo">
    <plugin
      filename="gz-sim-physics-system"
      name="gz::sim::systems::Physics">
    </plugin>
    <plugin
      filename="gz-sim-sensors-system"
      name="gz::sim::systems::Sensors">
      <render_engine>ogre2</render_engine>
    </plugin>
    <plugin
      filename="gz-sim-scene-broadcaster-system"
      name="gz::sim::systems::SceneBroadcaster">
    </plugin>
    <plugin
      filename="gz-sim-user-commands-system"
      name="gz::sim::systems::UserCommands">
    </plugin>

    <light name="sun" type="directional">
      <cast_shadows>true</cast_shadows>
      <pose>0 0 10 0 0 0</pose>
      <diffuse>0.8 0.8 0.8 1</diffuse>
      <specular>0.2 0.2 0.2 1</specular>
      <attenuation>
        <range>1000</range>
        <constant>0.9</constant>
        <linear>0.01</linear>
        <quadratic>0.001</quadratic>
      </attenuation>
      <direction>-0.5 0.1 -0.9</direction>
    </light>

    <model name="ground_plane">
      <static>true</static>
      <link name="link">
        <collision name="collision">
          <geometry>
            <plane>
              <normal>0 0 1</normal>
              <size>100 100</size>
            </plane>
          </geometry>
        </collision>
        <visual name="visual">
          <geometry>
            <plane>
              <normal>0 0 1</normal>
              <size>100 100</size>
            </plane>
          </geometry>
          <material>
            <ambient>0.8 0.8 0.8 1</ambient>
            <diffuse>0.8 0.8 0.8 1</diffuse>
            <specular>0.8 0.8 0.8 1</specular>
          </material>
        </visual>
      </link>
    </model>
    <include>
      <uri>model://crazyflie</uri>
      <name>crazyflie</name>
      <pose>0.0 0.0 0 0 0 -1.57</pose>
    </include>

    <model name="top_wall"> 
      <pose>2 -1 0.5 0 0 0</pose>
      <static>true</static>
      <link name="link">
        <visual name="visual">
          <geometry>
            <box>
              <size>0.2 6 2</size>
            </box>
          </geometry>
        </visual>
      </link>
    </model>

    <model name="bottom_wall">
      <pose>-2 0 0.5 0 0 0</pose>
      <static>true</static>
      <link name="link">
        <visual name="visual">
          <geometry>
            <box>
              <size>0.2 4 2</size>
            </box>
          </geometry>
        </visual>
      </link>
    </model>

    <model name="left_wall">
      <pose>0 2 0.5 0 0 1.57</pose>
      <static>true</static>
      <link name="link">
        <visual name="visual">
          <geometry>
            <box>
              <size>0.2 4 2</size>
            </box>
          </geometry>
        </visual>
      </link>
    </model>

    <model name="top_right_wall">
      <pose>1 -4 0.5 0 0 1.57</pose>
      <static>true</static>
      <link name="link">
        <visual name="visual">
          <geometry>
            <box>
              <size>0.2 2 2</size>
            </box>
          </geometry>
        </visual>
      </link>
    </model>

    <model name="bottom_right_wall">
      <pose>-1 -2 0.5 0 0 1.57</pose>
      <static>true</static>
      <link name="link">
        <visual name="visual">
          <geometry>
            <box>
              <size>0.2 2 2</size>
            </box>
          </geometry>
        </visual>
      </link>
    </model>

    <model name="middle_wall">
      <pose>0 -3 0.5 0 0 0</pose>
      <static>true</static>
      <link name="link">
        <visual name="visual">
          <geometry>
            <box>
              <size>0.2 2 2</size>
            </box>
          </geometry>
        </visual>
      </link>
    </model>
  </world>
</sdf>
```

## Textured wall room

> !!!!!!CHANGE THE DIRECTORY OF THE WALL TEXTURE IMAGE!!!!!!

```
<?xml version="1.0" ?>

<sdf version="1.8">
  <world name="demo">
    <plugin
      filename="gz-sim-physics-system"
      name="gz::sim::systems::Physics">
    </plugin>
    <plugin
      filename="gz-sim-sensors-system"
      name="gz::sim::systems::Sensors">
      <render_engine>ogre2</render_engine>
    </plugin>
    <plugin
      filename="gz-sim-scene-broadcaster-system"
      name="gz::sim::systems::SceneBroadcaster">
    </plugin>
    <plugin
      filename="gz-sim-user-commands-system"
      name="gz::sim::systems::UserCommands">
    </plugin>

    <light name="sun" type="directional">
      <cast_shadows>true</cast_shadows>
      <pose>0 0 10 0 0 0</pose>
      <diffuse>0.8 0.8 0.8 1</diffuse>
      <specular>0.2 0.2 0.2 1</specular>
      <attenuation>
        <range>1000</range>
        <constant>0.9</constant>
        <linear>0.01</linear>
        <quadratic>0.001</quadratic>
      </attenuation>
      <direction>-0.5 0.1 -0.9</direction>
    </light>

    <model name="ground_plane">
      <static>true</static>
      <link name="link">
        <collision name="collision">
          <geometry>
            <plane>
              <normal>0 0 1</normal>
              <size>100 100</size>
            </plane>
          </geometry>
        </collision>
        <visual name="visual">
          <geometry>
            <plane>
              <normal>0 0 1</normal>
              <size>100 100</size>
            </plane>
          </geometry>
          <material>
            <ambient>0.8 0.8 0.8 1</ambient>
            <diffuse>0.8 0.8 0.8 1</diffuse>
            <specular>0.8 0.8 0.8 1</specular>
          </material>
        </visual>
      </link>
    </model>
    <include>
      <uri>model://crazyflie</uri>
      <name>crazyflie</name>
      <pose>0.0 0.0 0 0 0 -1.57</pose>
    </include>

    <model name="wall1">
      <pose>2 0 0.5 0 0 0</pose>
      <static>true</static>
      <link name="link">
        <visual name="visual">
          <geometry>
            <box>
              <size>0.2 4 2</size>
            </box>
          </geometry>
          <material>
            <ambient>1 1 1 1</ambient>
            <diffuse>1 1 1 1</diffuse>
            <pbr>
              <metal>
                <albedo_map>file:///home/odyssey/final-project/crazyflie_mapping_demo/ros2_ws/src/cf-gz/ros_gz_crazyflie_gazebo/worlds/wall_texture.png</albedo_map>
              </metal>
            </pbr>
          </material>
        </visual>
      </link>
    </model>

    <model name="wall2">
      <pose>-2 0 0.5 0 0 0</pose>
      <static>true</static>
      <link name="link">
        <visual name="visual">
          <geometry>
            <box>
              <size>0.2 4 2</size>
            </box>
          </geometry>
          <material>
            <ambient>1 1 1 1</ambient>
            <diffuse>1 1 1 1</diffuse>
            <pbr>
              <metal>
                <albedo_map>file:///home/odyssey/final-project/crazyflie_mapping_demo/ros2_ws/src/cf-gz/ros_gz_crazyflie_gazebo/worlds/wall_texture.png</albedo_map>
              </metal>
            </pbr>
          </material>
        </visual>
      </link>
    </model>

    <model name="wall3">
      <pose>0 2 0.5 0 0 1.57</pose>
      <static>true</static>
      <link name="link">
        <visual name="visual">
          <geometry>
            <box>
              <size>0.2 4 2</size>
            </box>
          </geometry>
          <material>
            <ambient>1 1 1 1</ambient>
            <diffuse>1 1 1 1</diffuse>
            <pbr>
              <metal>
                <albedo_map>file:///home/odyssey/final-project/crazyflie_mapping_demo/ros2_ws/src/cf-gz/ros_gz_crazyflie_gazebo/worlds/wall_texture.png</albedo_map>
              </metal>
            </pbr>
          </material>
        </visual>
      </link>
    </model>

    <model name="wall4">
      <pose>0 -2 0.5 0 0 1.57</pose>
      <static>true</static>
      <link name="link">
        <visual name="visual">
          <geometry>
            <box>
              <size>0.2 4 2</size>
            </box>
          </geometry>
          <material>
            <ambient>1 1 1 1</ambient>
            <diffuse>1 1 1 1</diffuse>
            <pbr>
              <metal>
                <albedo_map>file:///home/odyssey/final-project/crazyflie_mapping_demo/ros2_ws/src/cf-gz/ros_gz_crazyflie_gazebo/worlds/wall_texture.png</albedo_map>
              </metal>
            </pbr>
          </material>
        </visual>
      </link>
    </model>
  </world>
</sdf>
```