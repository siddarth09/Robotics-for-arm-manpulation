# Robotics-for-arm-manpulation

## Kinematics:
Robot kinematics applies geometry to the study of the movement of multi-degree of freedom kinematic chains that form the structure of robotic systems. The Kinematics is most importantly used to find the position, orientation, velocity, force and torque(dynamics) for the robot end effector with respect to the base frame

## HOW TO FIND ROBOT KINEMATICS (FORWARD)
> The Robot kinematics can be found in three simple ways
  1. First define Universal coordinate system and assign the axes to the robot joints ( including to end effector)
  2. Using `Denavit-Hartenberg`notation assign the DH-Parameters for the robot link
  3. Using the DH-parameter table, find transformation matrix

### DH-PARAMETERS

NOTATION          |       DEFINITION
------------------|-------------------
1.Theta           | The angle from Xi-1 to Xi axes measured about the Z axis
2.Offset-Distance | The distance from Xi-1 to Xi measured along Z axis
3.Angle of Twist  | The angle from Zi to Zi+1 measured about X axis
4.Link Length     | The distance from Zi to Zi+1 measured along X axis


## SAMPLE INPUT AND OUTPUT
```bash
DH TABLE
60 0 0 24
45 0 180 30
```
```bash

++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++ DH PARAMETER TABLE FOR 2 LINK ROBOT+++
++++++++++++++++++++++++++++++++++++++++++++++++
FRAME||THETA ||Dist ||ALPHA  ||A
1    || 60.0 || 0.0 || 0.0   || 24.0
2    || 45.0 || 0.0 || 180.0 || 30.0
++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++FORWARD KINEMATICS+++++++++++++++++

[[  0.52532199  -0.50923178  -0.6817036   15.75965966]
 [ -0.85090352  -0.31438423  -0.4208631  -25.52710574]
 [  0.           0.80115264  -0.59846007   0.        ]
 [  0.           0.           0.           1.        ]]
```
## INVERSE KINEMATICS

Inverse Kinematics is mainly used to find the link angle of the robotic arm manipulator, given we know the desired x and y position of the object. Here we have assumed the initial position of the robot end effector to be (0,0) ie; the origin. Using alegbraic equations the inverse kinematic of the end effector can be found.
also this inverse kinematics is for the 3-DOF arm with 2 links. 4 DOF and 6 DOF kinematics will be added later 
```bash
#SAMPLE INPUT 
3 4 4 5
#SAMPLE OUTPUT
LINK ANGLE 1 = -0.5181732776252194, LINK ANGLE 2 = 2.168202743440247


```
NOTE:
> plotting the arm using matplot will be added soon
