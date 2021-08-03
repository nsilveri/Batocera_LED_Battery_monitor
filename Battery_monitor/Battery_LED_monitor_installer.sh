#!/bin/sh
wget get-pip.py
pip install ads1115
bash batocera-save-overlay
wget battery_monitor.py
mv custom.sh /userdata/system
bash batocera-save-overlay