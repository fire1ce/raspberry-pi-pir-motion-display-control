#!/bin/bash

sudo systemctl disable motion-screen-control.service
sudo systemctl stop motion-screen-control.service
sudo rm -rf /etc/systemd/system/motion-screen-control.service
sudo rm -rf /usr/local/bin/motion-screen-control.py

echo "done."
