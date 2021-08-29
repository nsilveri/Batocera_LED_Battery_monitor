#import RPi.GPIO as GPIO
from gpiozero import PWMLED
from time import sleep
from signal import pause
import ADS1115
import time
import os

pwm_led_green = PWMLED(21)
pwm_led_red = PWMLED(23)

CURRENT_STATE = 0

VOLT100 = 4100
VOLT75	= 3750
VOLT50 	= 3650
VOLT25	= 3500
VOLT10	= 3300
VOLT0	= 3250

ads = ADS1115.ADS1115()
#STARTUP PROCEDURE----------> It can help you understand if the script starts correctly
pwm_led_green.value = 1
time.sleep(1)

pwm_led_green.value = 1
pwm_led_red.value = 0

for(i=0; i<10; i++)
    pwm_led_green.value = pwm_led_green.value - 0.1
    pwm_led_red.value = pwm_led_red.value + 0.1
    delay(0.1)

#END STARTUP PROCEDURE

while True:
    #The voltage is read 3 times and averaged, battery V+ is connected to the ADS1115 channel 1
    volt_1 = ads.readADCSingleEnded()
    volt_2 = ads.readADCSingleEnded()
    volt_3 = ads.readADCSingleEnded()
    volt = (volt_1 + volt_2 + volt_3) / 3
    #ADS1115 channel 2 is connected to the TinkerBoy charge led, it helps to understand if the Game boy is charging or not
    charge = ads.readADCSingleEnded(2)
    
    if(volt >= VOLT75 and CURRENT_STATE != 4): #GREEN LED turns ON
       #GREEN LED
       pwm_led_green.value = 1
       pwm_led_red.value = 0
       CURRENT_STATE = 4
    if(volt < VOLT75 and volt > VOLT50 and CURRENT_STATE != 3): #YELLOW LED turns on, the YELLOW LED is obtained by turning on the GREEN LED with half brightness and RED LED with full brightness at the same time
       #YELLOW LED
       pwm_led_green.value = 0.5
       pwm_led_red.value = 1
       CURRENT_STATE = 3
    if(volt < VOLT50 and volt > VOLT25 and CURRENT_STATE != 2): #ORANGE LED turns on, the ORANGE LED is obtained by turning on the GREEN LED with 1/10 brightness and RED LED with full brightness at the same time
       #ORANGE LED
       pwm_led_green.value = 0.1
       pwm_led_red.value = 1
       CURRENT_STATE = 2
    if(volt < VOLT25 and volt > VOLT10  and CURRENT_STATE != 1):
       #RED LED
       pwm_led_green.value = 0
       pwm_led_red.value = 1
       CURRENT_STATE = 1
    if(volt < VOLT10 and volt > VOLT0):
       #RED LED intermittently
       if(pwm_led_green.value != 0)
           pwm_led_green.value = 0
       pwm_led_red.value = 1
       time.sleep(1)
       pwm_led_red.value = 0
       if(CURRENT_STATE != 0)
           CURRENT_STATE = 0
    if(volt < VOLT0 and charge < 4000): #
       os.system('shutdown -h now')
    
    #print("{:.0f} mV on AN0".format(volt))
    
    time.sleep(1)

