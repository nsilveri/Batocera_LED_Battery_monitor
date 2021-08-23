#!/bin/sh
#FILE_1=/userdata/Battery_monitor/Battery_LED_monitor_TinkerBoy_installer.sh
#FILE_2=/userdata/Battery_monitor/Battery_LED_monitor_installer.sh
if test -f "/userdata/Battery_monitor/Battery_LED_monitor_TinkerBoy_installer.sh"; then
    echo "$FILE_1 old script found."
	rm Battery_LED_monitor_TinkerBoy_installer.sh
	echo "Downloading last "LED_monitor_TinkerBoy_installer" script version..."
	wget https://raw.githubusercontent.com/nsilveri/Batocera_LED_Battery_monitor/main/Battery_monitor/Battery_LED_monitor_TinkerBoy_installer.sh
else
  wget https://raw.githubusercontent.com/nsilveri/Batocera_LED_Battery_monitor/main/Battery_monitor/Battery_LED_monitor_TinkerBoy_installer.sh
fi


if test -f "Battery_LED_monitor_installer.sh"; then
    echo "Battery_LED_monitor_installer.sh old script found."
	rm Battery_LED_monitor_installer.sh
	echo "Downloading last "LED_monitor_installer" script version..."
	wget https://raw.githubusercontent.com/nsilveri/Batocera_LED_Battery_monitor/main/Battery_monitor/Battery_LED_monitor_installer.sh
else
  wget https://raw.githubusercontent.com/nsilveri/Batocera_LED_Battery_monitor/main/Battery_monitor/Battery_LED_monitor_installer.sh
fi

if test -f "Battery_monitor.py"; then
    echo "Battery_monitor.py old script found."
	rm Battery_monitor.py
	echo "Downloading last Battery_monitor.py script version..."
	wget https://raw.githubusercontent.com/nsilveri/Batocera_LED_Battery_monitor/main/Battery_monitor/Battery_monitor.py
else
  wget https://raw.githubusercontent.com/nsilveri/Batocera_LED_Battery_monitor/main/Battery_monitor/Battery_monitor.py
fi

bash Battery_LED_monitor_TinkerBoy_installer.sh
