from gpiozero import MotionSensor
from signal import pause
from threading import Timer
import os

pir = MotionSensor(17)


def screenOn():
    print("Motion, turning the screen on")


while(True):
    pir.when_motion = screenOn


# def screenOff():
#     print("turning the screen off")


# def newTimer():
#     global timer
#     timer = Timer(10.0, screenOff)


# newTimer()


# def screenOn():
#     timer.cancel()
#     newTimer()
#     print("Motion, turning the screen on")


#     screenOn()
