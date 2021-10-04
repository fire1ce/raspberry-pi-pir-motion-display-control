#!/bin/bash

curl -O https://raw.githubusercontent.com/fire1ce/raspberry-pi-pir-motion-screen-control/main/motion-screen-control.py
curl -O https://raw.githubusercontent.com/fire1ce/raspberry-pi-pir-motion-screen-control/main/motion-screen-control.service

if [ ! -d "/usr/local/bin" ]; then
  sudo mkdir -p /usr/local/bin
fi

sudo chmod +x motion-screen-control.py
sudo mv motion-screen-control.py /usr/local/bin
sudo mv motion-screen-control.service /etc/systemd/system
sudo systemctl start motion-screen-control.service
sudo systemctl enable motion-screen-control.service

echo "done."
