#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# initialize robot
left = Motor(Port.C)
right = Motor(Port.B)
robot = DriveBase(left, right, 56, 114)

# initialize color sensor 
colorSensor = ColorSensor(Port.S3)

# communicates with users to get readings for sensors
# in order to calibrate the sensors 
def calibrateColorSensor(position = ""):
    while not any (brick.buttons()):
        brick.display.text("Place so that color ", (5, 50))
        brick.display.text("sensor hovers over")
        brick.display.text(position)
        brick.display.text("then press")
        brick.display.text("any button")
    reading = colorSensor.ambient()
    wait(100)
    brick.display.clear()
    wait(100)
    return reading

# actually retrieve the readings for the color sensors
def init():
    insideOfLine = calibrateColorSensor("center of line")
    print(str(insideOfLine))
    outsideOfLine = calibrateColorSensor("white section")
    print(str(outsideOfLine))
    edgeOfLine = ((insideOfLine + outsideOfLine) / 2)
    return edgeOfLine

# movement of the little bot
def inchWorm(edgeOfLine = 50,
            speed = 50,
            mSeconds = 100,
            direction = 0): 

    position = colorSensor.ambient()
    right = 45
    left = -45

    # if it's brighter, turn towards the line
    if position > edgeOfLine:
        direction = left
        print("left" + str(position))
    # if it's darker, turn away from the line
    elif position < edgeOfLine:
        direction = right
        print("right" + str(position))
    # if the porridge is juuuust right, follow the line
    else:
        direction = 0
        print("straight" + str(position))
    robot.drive_time(speed, direction, mSeconds)

# the action!
def runAlong(edgeOfLine: 0):
    # 0 to 200, 
    # because 200 iterations * 100 mSecs = 20 seconds
    for x in range(0, 200):
        inchWorm(edgeOfLine)

# use input to run along!
edgeOfLine = init()

# get the robot positioned
while not any (brick.buttons()):
    brick.display.text("position over edge", (5, 50))
    brick.display.text("of line and")
    brick.display.text("press any button")
    wait(100)

runAlong(edgeOfLine)
