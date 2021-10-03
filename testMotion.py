import subprocess

def getScreenStatus():
    vcgencmdDisplayPower = subprocess.run(['vcgencmd', 'display_power'], capture_output=True, text=True).stdout.strip()
    if (vcgencmdDisplayPower == "display_power=1"):
        return True
    else:
        return False

print(getScreenStatus())