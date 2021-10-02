#!/usr/bin/python3

from gpiozero import MotionSensor
from signal import pause
import os

pir = MotionSensor(17)

while True:

    pir.wait_for_motion()
    print("Motion detected!")

    pir.wait_for_no_motion(10)
    print("no motion for 10 seconds")


pause()
