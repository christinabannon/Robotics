#!/usr/bin/env pybricks-micropython
import math
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase


# initiate motors
leftMotor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
rightMotor = Motor(Port.B, Direction.COUNTERCLOCKWISE)

powerL = 50
powerR = 47.61
powerR15 = powerR * 1.15
time15cm = 815    
wheelDiameter = 5.6 # centimeters
baseLine = 11.4     # centimeters

# leftMotor.reset_angle(0)
# rightMotor.reset_angle(0)

# leftMotor.dc(powerL)
# rightMotor.dc(powerR)
# wait(time15cm)

# leftMotor.stop()
# rightMotor.stop()

def degreesToDistance(rotationAngleDegrees = 360, diameter = 5.6):
    circumference = math.pi * diameter
    totalRotations =  rotationAngleDegrees / 360 
    distanceTraveled = circumference * totalRotations
    return distanceTraveled


print("360 degrees, 10 cm diameter")
distance = degreesToDistance(360, 1)
print(distance)
leftDegrees = leftMotor.angle()
rightDegrees = rightMotor.angle()

print("left ")
print(str(leftDegrees))
print("right ")
print(str(rightDegrees))





