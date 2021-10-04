# Raspberry Pi Display Control Based on Motion (PIR) Sensor

## Information

This script uses pin GPIO4(7) to read data from Motion (PIR) Sensor, Any 5v and ground for PIR Sensor

![gpio layout](https://github.com/fire1ce/raspberry-pi-pir-motion-display-control/raw/main/gpio_layout.jpg)

![raspberrypi-with-PIR-sensor](https://github.com/fire1ce/raspberry-pi-pir-motion-display-control/raw/main/raspberrypi-with-PIR-sensor.jpg)

## Requirements

* python3-gpiozero

Can be install via apt

```bash
sudo apt install python3-gpiozero
```

## Install

This will install the script as `service` and it will run at boot

```bash
curl https://raw.githubusercontent.com/fire1ce/raspberry-pi-pir-motion-display-control/main/install.sh | bash
```

## Uninstall

```bash
curl https://raw.githubusercontent.com/fire1ce/raspberry-pi-pir-motion-display-control/main/uninstall.sh | bash
```

## Default Behavior

| __Condition__               | __Behavior__                        |
| --------------------------- | ----------------------------------- |
| Motion while display is off | Turns on display for 60 sec         |
| Motion while display is on  | Resets the timer for another 60 sec |
| No motion > 60 sec          | Turns off the display               |

## Config

File

```bash
/usr/local/bin/motion-display-control.py
```

You can change Data Pin of the PIR Sensor at __gpio_pin__ value
You can change Delay at __display_delay__ value

Line

```python
motion = Motion(gpio_pin=4, display_delay=60, verbose=False)
```

Restart the service to apply changes

```bash
sudo systemctl restart power_button.service
```

## Debug

In order to allow verbose debug change the following

File

```bash
/usr/local/bin/motion-display-control.py
```

Line

Set __verbose__ value to __True__

```python
motion = Motion(gpio_pin=4, display_delay=60, verbose=True)
```

Restart the service to apply changes

```bash
sudo systemctl restart power_button.service
```

## Check if service is running

```bash
sudo systemctl status power_button.service
```

## Contributors

Thanks to [Boris Berman
](https://github.com/bermanboris/raspberry-pi-pir-motion-display-control) for the script rewrite from function to classes
