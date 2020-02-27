#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# initiate color sensors
leftColorSensor = ColorSensor(Port.S2)
rightColorSensor = ColorSensor(Port.S3)

# initiate motors
leftMotor = Motor(Port.C)
rightMotor = Motor(Port.B)
speed = 200

# initiate our test boolean to false, 
# once aligned program can end
aligned = False

# If the right sensor has already detected a black line, 
# this method will position the robot so that the left sensor 
# will also find the black line
def rightStopLeftAlign( slowMo = speed / 2,
                       slowReverse = -1 * speed / 4 ):
    rightMotor.stop()
    aligned = (leftColorSensor.color() == Color.BLACK)
    while not aligned:
        leftMotor.run(slowMo)
        rightMotor.run(slowReverse)
        leftColorReading = leftColorSensor.color()
        rightColorReading = rightColorSensor.color()
        aligned = (rightColorReading == Color.BLACK) and (leftColorReading == Color.BLACK)
    return aligned

# If the left sensor has already detected a black line, 
# this method will position the robot so that the right sensor 
# will also find the black line
def leftStopRightAlign( slowMo = speed / 2,
                        slowReverse = -1 * speed / 4 ):
    leftMotor.stop()
    aligned = rightColorSensor.color() == Color.BLACK
    while not aligned: 
        rightMotor.run(slowMo)
        leftMotor.run(slowReverse)
        rightColorReading = rightColorSensor.color()
        leftColorReading = leftColorSensor.color()
        aligned = (leftColorReading == Color.BLACK) and (rightColorReading == Color.BLACK) 
    return aligned

#loop to keep motors searching before any black has been detected
while not aligned:
    leftMotor.run(1.05*speed) #left motor is slightly slower than right
    rightMotor.run(speed)
    wait(1)
    if (rightColorSensor.color() == Color.BLACK):
        aligned = rightStopLeftAlign()
    elif (leftColorSensor.color() == Color.BLACK): 
        aligned = leftStopRightAlign()

# line found, motors stop
leftMotor.stop() 
rightMotor.stop()


