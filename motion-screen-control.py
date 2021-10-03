from gpiozero import MotionSensor
from signal import pause
from threading import Timer
import os

pir = MotionSensor(17)


def screenoff():
    print("screenoff")

def newTimer():
    print("newTimer")
    global timer
    timer = Timer(10.0, screenoff)
    timer.start()

newTimer()

def screenOn():
    timer.cancel()
    newTimer()
    print("Motion, turning the screen on")

while True:
    pir.when_motion = screenOn
