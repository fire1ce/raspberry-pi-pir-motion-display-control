#!/bin/bash

curl -O https://raw.githubusercontent.com/fire1ce/raspberry-pi-pir-motion-display-control/main/motion-display-control.py
curl -O https://raw.githubusercontent.com/fire1ce/raspberry-pi-pir-motion-display-control/main/motion-display-control.service

if [ ! -d "/usr/local/bin" ]; then
  sudo mkdir -p /usr/local/bin
fi

sudo chmod +x motion-display-control.py
sudo mv motion-display-control.py /usr/local/bin
sudo mv motion-display-control.service /etc/systemd/system
sudo systemctl start motion-display-control.service
sudo systemctl enable motion-display-control.service

echo "done."
