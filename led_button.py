import wiringpi
import time
import subprocess

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
wiringpi.digitalWrite(r_led_pin,1)
pr2=subprocess.Popen("python3 ./send.py")

while True:
    if wiringpi.digitalRead(b_pin)==0 :
        f = True
        for i in range(3):
            wiringpi.digitalWrite(g_led_pin,1)
            time.sleep(0.5)
            wiringpi.digitalWrite(g_led_pin,0)
            time.sleep(0.5)
            if wiringpi.digitalRead(b_pin)==0:
                pass
            else:
                f = False
                break
        if f:
            pr2.terminate()
            wiringpi.digitalWrite(g_led_pin,1)
            pr1=subprocess.Popen("python3 ./con/web_api.py")
            pr1.wait()
            wiringpi.digitalWrite(g_led_pin,0)
            pr2=subprocess.Popen("python3 ./send.py")
    time.sleep(0.1)
pr2.terminate()



