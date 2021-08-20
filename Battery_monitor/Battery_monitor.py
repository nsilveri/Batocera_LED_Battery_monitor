from gpiozero import PWMLED
from time import sleep
from signal import pause
import ADS1115
import time
import os

pwm_led_green = PWMLED(21)
pwm_led_red = PWMLED(23)

VOLT100 = 4100
VOLT75	= 3750
VOLT50 	= 3650
VOLT25	= 3500
VOLT10	= 3300
VOLT0	= 3250

ads = ADS1115.ADS1115()
#STARTUP PROCEDURE----------> It can help you understand if the script starts correctly
#print("GREEN on")
pwm_led_green.value = 1
time.sleep(1)

#print("GREEN off")
pwm_led_green.value = 0
time.sleep(1)

#print("YELLOW on")
pwm_led_green.value = 0.2 #0.2 ---> 20% brightness
pwm_led_red.value = 1
time.sleep(1)

#print("YELLOW off")
pwm_led_green.value = 0
pwm_led_red.value = 0
time.sleep(1)

#print("RED on")
pwm_led_red.value = 1
time.sleep(1)

#print("RED off")
pwm_led_red.value = 0
time.sleep(1)

#END STARTUP PROCEDURE

while True:
    #The voltage is read 3 times and averaged, battery V+ is connected to the ADS1115 channel 1
    volt_1 = ads.readADCSingleEnded()
    volt_2 = ads.readADCSingleEnded()
    volt_3 = ads.readADCSingleEnded()
    volt = (volt_1 + volt_2 + volt_3) / 3
    #ADS1115 channel 2 is connected to the TinkerBoy charge led, it helps to understand if the Game boy is charging or not
    charge = ads.readADCSingleEnded(2)
    
    if(volt >= VOLT75): #GREEN LED turns ON
       pwm_led_green.value = 1 #1 ---> Green 100% brightness
       pwm_led_red.value = 0 #0 ---> Red 0% brightness / led off
        
    if(volt < VOLT75 and volt > VOLT50): #the GREEN LED alternates with the YELLOW LED, the YELLOW LED is obtained by turning on the GREEN and RED LED at the same time
       #GREEN LED 
       pwm_led_green.value = 1
       pwm_led_red.value = 0 #0 ---> Red 0% brightness / led off
       time.sleep(1)
        
       #YELLOW LED
       pwm_led_green.value = 0.2 #0.2 ---> Green 20% brightness
       pwm_led_red.value = 1 #1 ---> Red 100% brightness
    
    if(volt < VOLT50 and volt > VOLT25):
       #YELLOW LED
       pwm_led_green.value = 0.2 #0.2 ---> Green 20% brightness
       pwm_led_red.value = 1 #1 ---> Red 100% brightness
    
    if(volt < VOLT25 and volt > VOLT10):
       #RED LED
       pwm_led_green.value = 0 #0 ---> Green 0% brightness / led off
       pwm_led_red.value = 1 #1 ---> Red 100% brightness
    
    if(volt < VOLT10 and volt > VOLT0):
       #RED LED intermittently
       pwm_led_green.value = 0 #0 ---> Green 0% brightness / led off
       pwm_led_red.value = 1 #1 ---> Red 100% brightness
       time.sleep(1)
       pwm_led_red.value = 0 #0 ---> Red 0% brightness / led off
    
    if(volt < VOLT0 and charge < 4000): #
       os.system('shutdown -h now')
    
    #print("{:.0f} mV mesuré sur AN0".format(volt))
    
    time.sleep(1)

