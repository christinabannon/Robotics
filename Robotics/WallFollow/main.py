#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# initialize robot
left = Motor(Port.B)
right = Motor(Port.C)
# robot = DriveBase(left, right, 56, 114)

# initialize Ultrasonic Sensor
ultrasonicSensor = UltrasonicSensor(Port.S4)

# take the average of 2 readings to get a better reading
def getDistance():
    distance1 = ultrasonicSensor.distance()
    distance2 = ultrasonicSensor.distance()
    distance = ((distance1 + distance2) / 2)
    return distance

def navigate(distance = 200,
            speed = -30,
            mSec = 200):

    # if it's really far from the wall
    if distance > 320:
        #turning towards the wall
        right.run(speed)
        left.run(-speed)
        wait(mSec)

        # both motors running
        left.run(speed)
        wait(8*mSec)

        # straightening out
        right.run(-speed)
        wait(mSec)
        left.stop()
        right.stop()

    # if it's kind of far from the wall
    elif distance > 220:
        #turning towards the wall
        right.run(speed)
        left.run(-speed)
        wait(mSec)

        # both motors running
        left.run(speed)
        wait(5*mSec)

        # straightening out
        right.run(-speed)
        wait(mSec)
        left.stop()
        right.stop()

    # if it's really close to the wall
    elif distance < 100:
        # turning away from the wall
        left.run(speed)
        right.run(-speed)
        wait(mSec)

        # both motors running
        right.run(speed)
        wait(8*mSec)

        # straightening out
        left.run(-speed)
        wait(mSec)
        right.stop()
        left.stop()

    # if it's kind of close to the wall
    elif distance < 200:
        # turning away from the wall
        left.run(speed)
        right.run(-speed)
        wait(mSec)

        # both motors running
        right.run(speed)
        wait(5*mSec)

        # straightening out
        left.run(-speed)
        wait(mSec)
        right.stop()
        left.stop()

    # if it's straight
    else:
        left.run(speed)
        right.run(speed)
        wait(mSec)
        left.stop()
        right.stop()

#for x in range(0, 200):
while(1):
    distanceFromSensor = getDistance()
    navigate(distanceFromSensor)