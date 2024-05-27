# Blink.py
# Code taken from the Electronics Starter Kit at MonkMakes.com

from gpiozero import LED
from signal import pause

red_led = LED(18)

#The first number in blink() is the on time and the second is off time (both in seconds)
red_led.blink(on_time=0.5, off_time=0.5)

pause()

#the pause() is needed at the end to keep the program running