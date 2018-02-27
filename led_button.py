import wiringpi
import time
import PRi.GPIO as GPIO
import os

g_led_pin=9
r_led_pin=11
b_pin=3

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(b_pin,0)
wiringpi.pinMode(r_led_pin,1)
wiringpi.pinMode(g_led_pin,1)
wiringpi.pullUpDnControl(b_pin,2)

for i in range(3):
    wiringpi.digitalWrite(r_led_pin,1)
    wiringpi.digitalWrite(g_led_pin,1)
    time.sleep(0.5)
    wiringpi.digitalWrite(r_led_pin,0)
    wiringpi.digitalWrite(g_led_pin,0)
    time.sleep(0.5)

while True:
    time.sleep(0.1)

