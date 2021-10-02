#!/usr/bin/python3

from gpiozero import MotionSensor
from signal import pause
import os


def motion():
    print("Motion detected!")


motion.wait_for_no_motion(10)
print("no motion for 10 seconds")


MotionSensor(17) = motion.wait_for_motion

pause()
