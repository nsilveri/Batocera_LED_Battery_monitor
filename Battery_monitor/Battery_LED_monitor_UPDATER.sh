#!/bin/sh
FILE_1=/userdata/Battery_monitor/Battery_LED_monitor_TinkerBoy_installer.sh
FILE_2=/userdata/Battery_monitor/Battery_LED_monitor_installer.sh
if test -f "$FILE_1"; then
    echo "$FILE_1 old script found."
	rm $FILE_1
	echo "Downloading last "LED_monitor_TinkerBoy_installer" script version..."
	wget https://raw.githubusercontent.com/nsilveri/Batocera_LED_Battery_monitor/main/Battery_monitor/Battery_LED_monitor_TinkerBoy_installer.sh
fi

if test -f "$FILE_2"; then
    echo "$FILE_2 old script found."
	rm $FILE_2
	echo "Downloading last "LED_monitor_installer" script version..."
	wget https://raw.githubusercontent.com/nsilveri/Batocera_LED_Battery_monitor/main/Battery_monitor/Battery_LED_monitor_installer.sh
fi

bash $FILE_2