import wiringpi
import time

g_led_pin=9
r_led_pin=11

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(r_led_pin,1)
wiringpi.pinMode(g_led_pin,1)

wiringpi.digitalWrite(r_led_pin,0)
wiringpi.digitalWrite(g_led_pin,0)

while True:
    wiringpi.digitalWrite(g_led_pin,1)
    time.sleep(1)
    wiringpi.digitalWrite(g_led_pin,0)
    time.sleep(0.5)

