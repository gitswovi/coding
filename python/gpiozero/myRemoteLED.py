#!/bin/python3

# From https://gpiozero.readthedocs.io/en/stable/remote_gpio.html

#import libraries
from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory2 = PiGPIOFactory(host='192.168.16.1')
#factory3 = PiGPIOFactory(host='192.168.1.4')

led_1 = LED(17)  # local pin
led_2 = LED(7, pin_factory=factory2)  # remote pin on one pi
#led_3 = LED(17, pin_factory=factory3)  # remote pin on another pi

while True:
    led_1.on()
    led_2.off()
#    led_3.on()
    sleep(1)
    led_1.off()
    led_2.on()
 #   led_3.off()
    sleep(1)