from gpiozero import MotionSensor
from signal import pause
from threading import Timer
from subprocess import run


pir = MotionSensor(4)  # PIR Sensor on GPIO4 pin 7
timer = None


def turnDisplayOff():  # Turns off the display after timer is ended
    run(['vcgencmd', 'display_power', '0'])
    print("Turning the display Off...")


def newTimer():
    global timer  # Number of seconds before turning the display off
    timer = Timer(60, turnDisplayOff)
    timer.start()


def getDisplayStatus():  # Return True if display is ON, False if display is off
    vcgencmdDisplayPower = run(
        ['vcgencmd', 'display_power'], capture_output=True, text=True).stdout.strip()
    if (vcgencmdDisplayPower == "display_power=1"):
        return True
    else:
        return False


newTimer()


def turnDisplayOn():
    timer.cancel()
    newTimer()
    if not (getDisplayStatus()):
        run(['vcgencmd', 'display_power', '1'])
        print("Turning the display On...")


turnDisplayOn()  # Initial state Display ON, turns off when no motion


pir.when_motion = turnDisplayOn
