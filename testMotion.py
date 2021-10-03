from gpiozero import MotionSensor
from signal import pause
from threading import Timer
import os

pir = MotionSensor(17)
pir.when_motion():
    print("works")

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


# while(True):

#     screenOn()
