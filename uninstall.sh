#!/bin/bash

sudo systemctl disable motion-display-control.service
sudo systemctl stop motion-display-control.service
sudo rm -rf /etc/systemd/system/motion-display-control.service
sudo rm -rf /usr/local/bin/motion-display-control.py

echo "done."
