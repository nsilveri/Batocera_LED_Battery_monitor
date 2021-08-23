# Batocera_LED_Battery_monitor
  
  Current version:
    
      - V0.3 [Added UPDATER scripts to reinstall the LED_Monitor when you change Batocera version]
      
  Older version:
  
      - V0.2 [now i use PWM to manage the individual LEDs, with pwm you can manage the LED's brightness too]
      - V0.1 [initial release]
  
  Video:
       ![GBA SP](https://github.com/nsilveri/Batocera_LED_Battery_monitor/blob/main/LED_Battery_monitor_GBA_SP.mp4)
       
       
  Prerequisites:
    
        -Raspberry Pi with installed Batocera
        -ADS1115 Module
  Installation: 
    
         1) Put the Battery_monitor folder in the /userdata directory in Batocera 
         2) If you use the TinkerBoy as power supply run the script "Battery_LED_monitor_TinkerBoy_installer.sh"
         3) If you don't use Tinkerboy run the script "Battery_LED_monitor_installer.sh"
         4) If everything goes well the raspberry pi will reboot and at the next boot, after the main screen of batocera has started, the LED will start flashing green, yellow and red and then settle on the color corresponding to the battery status
         NB: git clone doesn't work on Batocera, download the zip in Releases or clone it on your computer (if you clone you will clone the video too)
         NB2: every time you upgrade/downgrade your system to a later/earlier version you need to reinstall by running Battery_LED_monitor_TinkerBoy_installer_UPDATER.sh (if you have TinkerBoy) or Battery_LED_monitor_installer_UPDATER.sh (if you don't use TinkerBoy), it will provide to download the last version of installer's scripts.
 
 Directory where put folder:
 
 ![Directory where put folder](https://github.com/nsilveri/Batocera_LED_Battery_monitor/blob/main/images/directory.png)
 
    Directories must be:
     - /--->userdata--->Battery_monitor--+-->Battery_LED_monitor_installer.sh   <-----------+
                                         |                                                  |---[Run one of this two firstly]
                                         +-->Battery_LED_monitor_TinkerBoy_installer.sh  <--+
                                         |
                                         +-->Battery_LED_monitor_TinkerBoy_installer_UPDATER.sh <--+
                                         |                                                         |---[Run one of this two to upgrade scripts or when you upgrade the system]
                                         +-->Battery_LED_monitor_installer_UPDATER.sh  <-----------+
                                         |
                                         +-->Battery_monitor.py
                                         |
                                         +-->custom.sh
 
 My build:  
 
    - I used a case of a gameboy advance sp, leaving its motherboard to take advantage of its keys and its leds, in my case the 2 red and green leds are connected to pins 21 and 23 of the raspberry GPIO, if you use other PINs change them in the python script "Battery_monitor.py", having used the TinkerBoy to power everything,
    the orange led is connected directly to the TinkerBoy
 ADS1115:
 
    - The ADS1115 is powered directly by the TinkerBoy, the pins of the I2C (SDA and SCL) are connected to the respective GPIO PINs of the raspberry 
    - The channel 1 of the ADS1115 to the V + of the battery to read its voltage and calculate the state of charge of the battery and channel 2 to C + on the TinkerBoy to see if the device is charging or not
    
Next Version:

    - Make the scripts Recalbox compatible
    
   
    
  
