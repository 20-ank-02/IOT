# sudo raspi-config
# sudo reboot
# lsmod | grep spi
# sudo pip3 install spidev
# sudo pip3 install mfrc522

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        text = input('New data:')
        print("Now place your tag to write")
        reader.write(text)
        print("Written")
finally:
        GPIO.cleanup()