#!/usr/bin/python3

from gpiozero import MotionSensor
from signal import pause
from threading import Timer
import os

pir = MotionSensor(17)


def screenOff():
    print("turning the screen off")


def newTimer():
    print("newTimer")
    global timer
    timer = Timer(10.0, screenOff())
    timer.start()


newTimer()


def screenOn():
    timer.cancel()
    print("timerCancel")
    newTimer()
    print("Motion, turning the screen on")


while(True):
    pir.when_motion = screenOn

pause()
