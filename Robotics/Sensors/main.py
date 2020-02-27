#!/usr/bin/env pybricks-micropython

# test_Color.py
# Authors: Elizabeth Dellorco & Jennifer S. Kay, Rowan University
# 
# This work by Elizabeth Dellorco & Jennifer S. Kay 
# is licensed under the Creative Commons 
# Attribution-NonCommercial-ShareAlike 4.0 International License. 
# To view a copy of this license, visit 
# http://creativecommons.org/licenses/by-nc-sa/4.0/ 
#
# Written using EV3-Micropython 
#         
# All references are to the LEGO Education Getting Started with 
#   EV3 MicroPython version 1.0.0 documentation [EV3MPD]
#   from https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3
# 
# Code was tested using the EV3 Robot Educator model - instructions
#        for this build can be found at:
# https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot  
# 
# This code demonstrates the following EV3-Micropython Classes:
#      Class ColorSensor (see EV3MPD Chapter 4.2.2)
#      Class StopWatch (see EV3MPD Chapter 6)
#      Classmethod sound.file (see EV3MPD Chapter 3.3)
#   

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                        		 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                        		 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# # Initialize two motors with default settings on Port B and Port C.
# # These will be the left and right motors of the drive base.
# left_motor = Motor(Port.B)
# right_motor = Motor(Port.C)

# # The wheel diameter of the Robot Educator is 56 millimeters.
# wheel_diameter = 56

# # The axle track is the distance between the centers of each of the wheels.
# # For the Robot Educator this is 114 millimeters.
# axle_track = 114

# # The DriveBase is composed of two motors, with a wheel on each motor.
# # The wheel_diameter and axle_track values are used to make the motors
# # move at the correct speed when you give a motor command.
# robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)


#--------------------- Sensor Port Setup ----------------------------
# Super important - uncomment any sensors you are using!!!!
# Initialize the touch sensor in port 1
# touch_sensor = TouchSensor(Port.S1)

# Initialize the gyro sensor in port 2
# gyro_sensor = GyroSensor(Port.S2)

# # Initialize the color sensor in port A
# colorSensorS1 = ColorSensor(Port.S1)
# colorSensorS2 = ColorSensor(Port.S2)

# Initialize the ultrasonic sensor in port 4
obstacle_sensor = UltrasonicSensor(Port.S1)

###############################################################################
#######  		 Standard Initialization Code Ends Here        		  ######## 
###############################################################################


print(obstacle_sensor.distance())

