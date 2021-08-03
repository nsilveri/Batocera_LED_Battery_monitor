import RPi.GPIO as GPIO
import ADS1115
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

VOLT100 = 4100
VOLT75	= 3750
VOLT50 	= 3650
VOLT25	= 3500
VOLT10	= 3300
VOLT0	= 3250

ads = ADS1115.ADS1115()
#STARTUP PROCEDURE----------> It can help you understand if the script starts correctly
#print("GREEN on")
GPIO.output(21,GPIO.HIGH)
time.sleep(1)

#print("GREEN off")
GPIO.output(21,GPIO.LOW)
time.sleep(1)

#print("YELLOW on")
GPIO.output(21,GPIO.HIGH)
GPIO.output(23,GPIO.HIGH)
time.sleep(1)

#print("YELLOW off")
GPIO.output(21,GPIO.LOW)
GPIO.output(23,GPIO.LOW)
time.sleep(1)

#print("RED on")
GPIO.output(23,GPIO.HIGH)
time.sleep(1)

#print("RED off")
GPIO.output(23,GPIO.LOW)

#END STARTUP PROCEDURE

while True:
    #The voltage is read 3 times and averaged, battery V+ is connected to the ADS1115 channel 1
    volt_1 = ads.readADCSingleEnded()
    volt_2 = ads.readADCSingleEnded()
    volt_3 = ads.readADCSingleEnded()
    volt = (volt_1 + volt_2 + volt_3) / 3
    #ADS1115 channel 2 is connected to the TinkerBoy charge led, it helps to understand if the Game boy is charging or not
    charge = ads.readADCSingleEnded(2)
    
    if(volt >= VOLT75): #GREEN turns ON
       GPIO.output(23,GPIO.LOW)
       GPIO.output(21,GPIO.HIGH)
    if(volt < VOLT75 and volt > VOLT50):
       GPIO.output(23,GPIO.LOW)
       GPIO.output(21,GPIO.HIGH)
       time.sleep(1)
       GPIO.output(21,GPIO.HIGH)
       GPIO.output(23,GPIO.HIGH)
    if(volt < VOLT50 and volt > VOLT25):
       GPIO.output(21,GPIO.HIGH)
       GPIO.output(23,GPIO.HIGH)
    if(volt < VOLT25 and volt > VOLT10):
       GPIO.output(21,GPIO.LOW)
       GPIO.output(23,GPIO.HIGH)
    if(volt < VOLT10 and volt > VOLT0):
       GPIO.output(21,GPIO.LOW)
       GPIO.output(23,GPIO.HIGH)
       time.sleep(1)
       GPIO.output(23,GPIO.LOW)
    if(volt < VOLT0 and charge < 4000):
       os.system('shutdown -h now')
    
    #print("{:.0f} mV mesuré sur AN0".format(volt))
    
    time.sleep(1)
