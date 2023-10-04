#!/bin/sh

# Making boot writable
echo '>>> Making boot writable...'
mount -o remount,rw /boot

# Enable Safe Shutdown
echo '>>> Setting up Safe Shutdown...'
if grep -q 'dtoverlay=gpio-poweroff,gpiopin=10,active_low=1' /boot/config.txt; then
  echo 'Seems "poweroff" already exists, skipping this step.'
else
  poweroff="dtoverlay=gpio-poweroff,gpiopin=10,active_low=1"
  echo "$poweroff" >> /boot/config.txt
fi

if grep -q 'dtoverlay=gpio-shutdown,gpio_pin=11,active_low=1' /boot/config.txt; then
  echo 'Seems "shutdown" already exists, skipping this step.'
else
  shutdown="dtoverlay=gpio-shutdown,gpio_pin=11,active_low=1"
  echo "$shutdown" >> /boot/config.txt
fi

# Enable I2C
echo '>>> Enabling I2C...'
if grep -q 'i2c-bcm2837' /etc/modules.conf; then
  echo 'Seems i2c-bcm2837 module already exists, skipping this step.'
else
  echo 'i2c-bcm2837' >> /etc/modules.conf
fi

if grep -q 'i2c-dev' /etc/modules.conf; then
  echo 'Seems i2c-dev module already exists, skipping this step.'
else
  echo 'i2c-dev' >> /etc/modules.conf
fi

if grep -q 'dtparam=i2c1=on' /boot/config.txt; then
  echo 'Seems i2c1 parameter already set, skipping this step.'
else
  echo 'dtparam=i2c1=on' >> /boot/config.txt
fi

if grep -q 'dtparam=i2c_arm=on' /boot/config.txt; then
  echo 'Seems i2c_arm parameter already set, skipping this step.'
else
  echo 'dtparam=i2c_arm=on' >> /boot/config.txt
fi

if [ -f /etc/modprobe.d/raspi-blacklist.conf ]; then
  sed -i 's/^blacklist spi-bcm2837/#blacklist spi-bcm2837/' /etc/modprobe.d/raspi-blacklist.conf
  sed -i 's/^blacklist i2c-bcm2837/#blacklist i2c-bcm2837/' /etc/modprobe.d/raspi-blacklist.conf
else
  echo 'File raspi-blacklist.conf does not exist, skipping this step.'
fi

# Install Python PIP
echo '>>> Installing Python PIP...'
python -m ensurepip --upgrade

# Install gpiozero python library to use LEDs with PWM method
echo '>>> Installing gpiozero python library...'
pip3 install gpiozero

# Install Python ads1115 to read voltages values
echo '>>> Installing ads1115 python library...'
pip3 install ads1115

# Install oled_i2c python library
echo '>>> Installing oled_i2c python library...'
pip3 install adafruit-circuitpython-ssd1306

# Save Batocera Overlay
echo '>>> Saving Batocera Overlay...'
bash batocera-save-overlay

# Setting Script Startup
echo '>>> Autobooting script...'
cp custom.sh /userdata/system
bash batocera-save-overlay

echo '>>> Finish!!!'
reboot
