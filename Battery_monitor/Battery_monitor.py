#!/usr/bin/env python3
#LED control libraries
from gpiozero import PWMLED
from time import sleep
from signal import pause
import ADS1115
import time
import os
import logging
import OLED_info
'''
# Creazione del logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Creazione dell'handler per scrivere su file
log_file = '/userdata/Battery_monitor/logs.log'
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)

# Definizione del formato del messaggio di log
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

<<<<<<< HEAD
# Aggiunta dell'handler al logger
logger.addHandler(file_handler)

#try:
logger.info('Avvio Battery_monitor.py')
'''

GREEN_LED_PIN  = 21
RED_LED_PIN    = 23

pwm_led_green  = PWMLED(GREEN_LED_PIN)
pwm_led_red    = PWMLED(RED_LED_PIN)

CURRENT_STATE           = 5
BATTERY_LOW_CURRENT     = 15
LED_BLINK_BATTERY_LOW   = 0
BATTERY_PERCENTAGE_OLD  = 100
BATT_PERC               = 100

VOLT100     = 4200
VOLT75      = 3950
VOLT50      = 3700
VOLT25      = 3450
VOLT10      = 3350
VOLT5	      = 3250
VOLT0       = 3200
VOLT_ERROR  = 3000
=======
VOLT100 = 4200
VOLT75  = 3950
VOLT50  = 3700
VOLT25  = 3450
VOLT10  = 3350
VOLT5	= 3250
VOLT0   = 3200
>>>>>>> main

ads = ADS1115.ADS1115()
#STARTUP PROCEDURE----------> It can help you understand if the script starts correctly
#print("GREEN on")
#GPIO.output(21,GPIO.HIGH)
pwm_led_green.value = 1
time.sleep(1)

pwm_led_green.value = 1
pwm_led_red.value = 0

<<<<<<< HEAD
#oled_controller.message("Silver Boy 2.0", "Loading")

for i in range(10):
   pwm_led_green.value = pwm_led_green.value - 0.1
   pwm_led_red.value = pwm_led_red.value + 0.1
   time.sleep(0.1)
=======
for i in range(10):
    pwm_led_green.value = pwm_led_green.value - 0.1
    pwm_led_red.value = pwm_led_red.value + 0.1
    time.sleep(0.1)
>>>>>>> main

#oled_controller.message("Silver Boy 2.0", "Loading.")

for i in range(10):
<<<<<<< HEAD
   pwm_led_green.value = pwm_led_green.value + 0.1
   pwm_led_red.value = pwm_led_red.value - 0.1
   time.sleep(0.1)
=======
    pwm_led_green.value = pwm_led_green.value + 0.1
    pwm_led_red.value = pwm_led_red.value - 0.1
    time.sleep(0.1)
>>>>>>> main

#oled_controller.message("Silver Boy 2.0", "Loading..")

for i in range(10):
<<<<<<< HEAD
   pwm_led_green.value = pwm_led_green.value - 0.1
   pwm_led_red.value = pwm_led_red.value + 0.1
   time.sleep(0.1)
=======
    pwm_led_green.value = pwm_led_green.value - 0.1
    pwm_led_red.value = pwm_led_red.value + 0.1
    time.sleep(0.1)
>>>>>>> main

#oled_controller.message("Silver Boy 2.0", "Loading...")

for i in range(10):
<<<<<<< HEAD
   pwm_led_green.value = pwm_led_green.value + 0.1
   pwm_led_red.value = pwm_led_red.value - 0.1
   time.sleep(0.1)
=======
    pwm_led_green.value = pwm_led_green.value + 0.1
    pwm_led_red.value = pwm_led_red.value - 0.1
    time.sleep(0.1)
>>>>>>> main

#oled_controller.message("Silver Boy 2.0", "Loading....")

pwm_led_green.value = 0
pwm_led_red.value = 0

time.sleep(1)

#END STARTUP PROCEDURE

def _map(x, in_min, in_max, out_min, out_max):
   return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

while True:
   #The voltage is read 6 times and averaged, battery V+ is connected to the ADS1115 channel 1
   volt_array = [0, 0, 0, 0, 0, 0]
   current_volt = 0

   for i in range(len(volt_array)):
      volt_array[i] = ads.readADCSingleEnded()
      time.sleep(0.1)
   
   for i in range(len(volt_array)):
      current_volt = current_volt + volt_array[i]
   current_volt = current_volt / len(volt_array)
   '''
   volt_2 = ads.readADCSingleEnded()
   time.sleep(1)
   volt_3 = ads.readADCSingleEnded()
   time.sleep(1)
   '''
   #volt = (volt_1 + volt_2 + volt_3) / 3
   
   BATT_PERC_AUX = _map(current_volt, VOLT0, VOLT100, 0, 100)
   
   if(current_volt > VOLT_ERROR and BATTERY_PERCENTAGE_OLD > BATT_PERC_AUX):
      BATTERY_PERCENTAGE_OLD = BATT_PERC_AUX
      BATT_PERC = BATT_PERC_AUX
      print(BATT_PERC)

   #ADS1115 channel 2 is connected to the TinkerBoy charge led, it helps to understand if the Game boy is charging or not
   charge = ads.readADCSingleEnded(2)
   
   OLED_info.oled_info(current_volt)
   
   if(BATT_PERC > 75):#GREEN LED turns ON
      pwm_led_green.value = 1
      pwm_led_red.value = 0
      CURRENT_STATE = 4
   if(BATT_PERC < 75 and BATT_PERC > 50):#the GREEN LED alternates with the YELLOW LED, the YELLOW LED is obtained by turning on the GREEN and RED LED at the same time
      #YELLOW LED
      pwm_led_green.value = 0.5
      pwm_led_red.value = 1
      CURRENT_STATE = 3
   if(BATT_PERC < 50 and BATT_PERC > 25):
      #YELLOW LED
      pwm_led_green.value = 0.2
      pwm_led_red.value = 1
      CURRENT_STATE = 2
   if(BATT_PERC < 25 and BATT_PERC > 10):
      #RED LED
      pwm_led_green.value = 0
      pwm_led_red.value = 1
      CURRENT_STATE = 1
   if(BATT_PERC < 10 and BATT_PERC > 3):
      #RED LED intermittently
      pwm_led_green.value = 0
      pwm_led_red.value = 1
      time.sleep(1)
      pwm_led_red.value = 0
      if(CURRENT_STATE != 0):
         CURRENT_STATE = 0
   if(BATT_PERC <= 3 and charge < 4000):
      BATTERY_LOW_CURRENT = BATTERY_LOW_CURRENT  - 1

      if(LED_BLINK_BATTERY_LOW == 0):
         pwm_led_green.value = 0
         pwm_led_red.value   = 1
         LED_BLINK_BATTERY_LOW = 1
      else:
         pwm_led_green.value = 1
         pwm_led_red.value   = 0
         LED_BLINK_BATTERY_LOW = 0

      if(BATTERY_LOW_CURRENT == 0):
         os.system('shutdown -h now')
   
#except Exception as e:
   #logger.exception('Errore durante l\'avvio di Battery_monitor.py: ' + str(e))
   
   #print("{:.0f} mV mesurati su AN0".format(volt))
   
   #time.sleep(0.5)