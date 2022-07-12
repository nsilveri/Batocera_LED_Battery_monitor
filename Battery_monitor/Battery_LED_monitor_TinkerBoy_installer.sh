#!/bin/sh
#Making boot writable
echo '>>> Making boot writable...'
mount -o remount,rw /boot
#Enable Safe Shutdown
printf "\nSetting up Safe Shutdown...\n\n"
if grep -q 'poweroff="dtoverlay=gpio-poweroff,gpiopin=10,active_low=1"' /boot/config.txt; then
  echo 'Seems "poweroff" already exists, skip this step.'
else
  poweroff="dtoverlay=gpio-poweroff,gpiopin=10,active_low=1"
  sh -c "echo '$poweroff' >> /boot/config.txt"
fi
if grep -q 'shutdown="dtoverlay=gpio-shutdown,gpio_pin=11,active_low=1"' /boot/config.txt; then
  echo 'Seems "shutdown" already exists, skip this step.'
else
  shutdown="dtoverlay=gpio-shutdown,gpio_pin=11,active_low=1"
  sh -c "echo '$shutdown' >> /boot/config.txt"
fi

#Enable I2C
echo '>>> Enable I2C'
if grep -q 'i2c-bcm2708' /etc/modules.conf; then
  echo 'Seems i2c-bcm2708 module already exists, skip this step.'
else
  echo 'i2c-bcm2708' >> /etc/modules.conf
fi
if grep -q 'i2c-dev' /etc/modules.conf; then
  echo 'Seems i2c-dev module already exists, skip this step.'
else
  echo 'i2c-dev' >> /etc/modules.conf
fi
if grep -q 'dtparam=i2c1=on' /boot/config.txt; then
  echo 'Seems i2c1 parameter already set, skip this step.'
else
  echo 'dtparam=i2c1=on' >> /boot/config.txt
fi
if grep -q 'dtparam=i2c_arm=on' /boot/config.txt; then
  echo 'Seems i2c_arm parameter already set, skip this step.'
else
  echo 'dtparam=i2c_arm=on' >> /boot/config.txt
fi
if [ -f /etc/modprobe.d/raspi-blacklist.conf ]; then
  sed -i 's/^blacklist spi-bcm2708/#blacklist spi-bcm2708/' /etc/modprobe.d/raspi-blacklist.conf
  sed -i 's/^blacklist i2c-bcm2708/#blacklist i2c-bcm2708/' /etc/modprobe.d/raspi-blacklist.conf
else
  echo 'File raspi-blacklist.conf does not exist, skip this step.'
fi

#Install Python PIP
#echo '>>> Download get-pip.py'
#wget https://bootstrap.pypa.io/get-pip.py
echo '>>> Install Python PIP'
python -m ensurepip --upgrade
#Install gpiozero python library to use LEDs with PWM method
echo '>>> Install gpiozero python library'
pip install gpiozero
#Install Python ads1115 to read voltages values
echo '>>> Install ads1115 python library'
pip install ads1115
echo '>>> Save Batocera Overlay'
bash batocera-save-overlay

#Setting Script Startup
echo '>>> Autobooting script...'
cp custom.sh /userdata/system
bash batocera-save-overlay
echo '>>> Finish!!!'
reboot
