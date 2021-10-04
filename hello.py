from gpiozero import MotionSensor
pir = MotionSensor(4)  # PIR Sensor on GPIO4 pin 7


def hello():  # Turns off the display after timer is ended
    print("hi")


pir.when_motion = hello
