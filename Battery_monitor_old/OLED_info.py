#!/usr/bin/env python3
import time
import psutil as PS
import socket
import board
#import digitalio
import adafruit_ssd1306


import ADS1115
import time
import os

#ads = ADS1115.ADS1115()

#
from PIL import Image, ImageDraw, ImageFont

VOLT100  = 4100
VOLT0	 = 3200

#
KB=1024
MB=KB*1024
GB=MB*1024
#
WIDTH = 128
HEIGHT = 64
FONTSIZE = 16
#
LOOPTIME = 0.5
#
#oldtime = time.time()
# Examples for usage:
#    IP = get_ipv4_from_interface("eth0")
#    IP = get_ipv4_from_interface("wlan0")
#def get_ipv4_from_interface(interfacename):
#    res="IP ?"
#    try:
#        iface=PS.net_if_addrs()[interfacename]
#        for addr in iface:
#            if addr.family is socket.AddressFamily.AF_INET:
#                return "IP {0}".format(addr.address)
#    except:
#        return res
#    return res

# This looks for the first IPv4 address that is not on the
# loopback interface. There is no guarantee on the order of
# the interfaces in the enumeration. If you've multiple interfaces
# and want to ensure to get an IPv4 address from a dedicated adapter,
# use the previous method.
def get_ipv4():
    ifaces=PS.net_if_addrs()
    for key in ifaces:
        if (key!="lo"): # Ignore the loopback interface
            # if it's not loopback, we look for the first IPv4 address    
            iface = ifaces[key]
            for addr in iface:
                if addr.family is socket.AddressFamily.AF_INET:
                    return "IP {0}".format(addr.address)
    return "IP ?"
#
# Use for I2C.
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C)

# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box
draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)

padding = -2
top = padding
bottom = oled.height-padding
x = 0

# font = ImageFont.load_default()
font3 = ImageFont.truetype('PixelOperator.ttf', FONTSIZE)

TIME = 0.0

def _map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

def message(message_string):
    global x
    global top
    #boot_message_string = "Silver-Boy loading..."
    draw.rectangle((0,0,oled.width,oled.height), outline=0, fill=0)
    draw.text((x, top),             message_string,  font=font, fill=255)
    oled.image(image)
    oled.show()

#while True:
def oled_info(volt_bat):
    global x
    global top
    global TIME
    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,oled.width,oled.height), outline=0, fill=0)

    #volt_bat = ads.readADCSingleEnded()
    bat_perc = _map(volt_bat, VOLT0, VOLT100, 0, 100)
    BATT_PERC = "Bat: " + str(bat_perc) + "%"
    BATT_VOLT = str(round(volt_bat/1000, 2)) + "V"


    #IP = get_ipv4()
    # IP = get_ipv4_from_interface("eth0") # Alternative
    
    CPU = "CPU: {:.1f}%".format(round(PS.cpu_percent(),1))

    temps=PS.sensors_temperatures()
    TEMP= "{:.1f}°C".format(round(temps['cpu_thermal'][0].current,1))

    mem=PS.virtual_memory()
    MemUsage = "RAM: {:5d}/{:5d}MB".format(round((mem.used+MB-1)/MB),round((mem.total+MB-1)/MB))

    #root=PS.disk_usage("/")
    #Disk="Disk {:4d}/{:4d}GB".format(round((root.used+GB-1)/GB),round((root.total+GB-1)/GB))

    draw.text((x, top),             BATT_PERC,  font=font, fill=255)
    draw.text((x+60,top),  	        BATT_VOLT,  font=font, fill=255)
    draw.text((x, top+FONTSIZE),    CPU,        font=font, fill=255)
    draw.text((x+70,top+FONTSIZE),  TEMP,       font=font, fill=255)
    draw.text((x, top+2*FONTSIZE),  MemUsage,   font=font, fill=255)

    # Display image
    oled.image(image)
    oled.show()

    TIME = TIME + 0.5
    #print("X:" + str(x) + " | TOP: " + str(top))

    #method to prevent oled burn-in
    if(TIME == 50):
      if(x == 0):
        x = x + 2
        top = top + 2
      elif(x != 0):
        x = 0
        top = padding
      TIME = 0
    
    #time.sleep(LOOPTIME)