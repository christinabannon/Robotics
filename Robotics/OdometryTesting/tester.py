#!/usr/bin/env pybricks-micropython
import math
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase




def degreesToDistance(rotationAngleDegrees = 360.0, 
                  diameter = 56):
    circumference = math.pi * diameter
    # print(str(circumference))
    totalRotations =  rotationAngleDegrees / 360.0
    # print(str(totalRotations))
    distanceTraveled = circumference * totalRotations
    return distanceTraveled

def computePoseChange(rightWheelRotAngleDegrees = 360.0,
                  leftWheelRotAngleDegrees = 360.0,
                  wheelDiameter = 56,
                  baseLine = 114):

    # get distances
    distanceLeft = degreesToDistance(leftWheelRotAngleDegrees, wheelDiameter)
    distanceRight = degreesToDistance(rightWheelRotAngleDegrees, wheelDiameter)

    # get directional angle change (radians)
    directionalAngleChange = ((distanceRight - distanceLeft) / baseLine)

    # get the distance traveled by the center of the bot
    distanceTravelledCenter = ((distanceLeft + distanceRight) / 2)

    # get the change in x
    deltaX = -1 * distanceTravelledCenter *  math.sin(directionalAngleChange)

    # get the change in y
    deltaY = distanceTravelledCenter *  math.cos(directionalAngleChange)
    
    # round everything off
    deltaX = round(deltaX, 2)
    deltaY = round(deltaY, 2)
    directionalAngleChange = round(directionalAngleChange, 2)

    # return new position
    return (deltaX, deltaY, directionalAngleChange)

# initiate motors
leftMotor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
rightMotor = Motor(Port.C, Direction.COUNTERCLOCKWISE)

powerL = 50
powerR = 52.5
powerR15 = powerR * 1.15
time15cm = 900    
wheelDiameter = 56   # centimeters
baseLine = 114       # centimeters

# reset angle
leftMotor.reset_angle(0)
rightMotor.reset_angle(0)

# run
leftMotor.dc(powerL)
rightMotor.dc(powerR15)
wait(time15cm)

# hard stop
leftMotor.stop(Stop.BRAKE)
rightMotor.stop(Stop.BRAKE)

# get rotational angle
leftWheelRotAngleDegrees = leftMotor.angle()
rightWheelRotAngleDegrees = rightMotor.angle()

# get pose change
poseChange = computePoseChange(rightWheelRotAngleDegrees, leftWheelRotAngleDegrees, wheelDiameter, baseLine)

brick.display.text(" X = " + str(poseChange[0]), (10,50))
brick.display.text(" Y = " + str(poseChange[1]))
brick.display.text(" angle = " + str(poseChange[2]))

wait(10000)

