from threading import Timer
from subprocess import run
from gpiozero import MotionSensor
from signal import pause

class Display:
  def status():
    status = run(['vcgencmd', 'display_power'], capture_output=True, text=True).stdout.strip()
    return status == "display_power=1"

  def turnOn():
    run(['vcgencmd', 'display_power', '1'])

  def turnOff():
    run(['vcgencmd', 'display_power', '0'])


class Motion:
  display = Display()

  def __init__(self, gpio_pin, display_delay = 60):
    self.display_delay = display_delay
    self.pir = MotionSensor(gpio_pin)
    self.pir.when_motion = self.onMotion
    self.resetTimer()
    pause()

  def resetTimer(self):
    if self.timer: 
      self.timer.cancel()

    self.timer = Timer(self.display_delay, self.display.turnOff)

  def onMotion(self):
    if not self.display.status():
      self.display.turnOn()

    self.resetTimer()


motion = Motion(gpio_pin=4, display_delay=60)
