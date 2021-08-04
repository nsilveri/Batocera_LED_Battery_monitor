# Batocera_LED_Battery_monitor
  
  Prerequisites:
    
        -Raspberry Pi with installed Batocera
        -ADS1115 Module
  Installation: 
    
         1) Put the Battery_monitor folder in the /userdata directory in Batocera
         2) If you use the TinkerBoy as power supply run the script "Battery_LED_monitor_TinkerBoy_installer.sh"
         3) If you don't use Tinkerboy run the script "Battery_LED_monitor_TinkerBoy_installer.sh"
         4) If everything goes well the raspberry pi will reboot and at the next boot, after the main screen of batocera has started, the LED will start flashing green, yellow and red and then settle on the color corresponding to the battery status
 My build:     
 
    I used a case of a gameboy advance sp, leaving its motherboard to take advantage of its keys and its leds, in my case the 2 red and green leds are connected to pins 21 and 23 of the raspberry GPIO, if you use other PINs change them in the python script "Battery_monitor.py", having used the TinkerBoy to power everything,
    the orange led is connected directly to the TinkerBoy
   
    
  
