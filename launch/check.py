import wiringpi

b_pin=3

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(b_pin,0)
wiringpi.pullUpDnControl(b_pin,2)

print("true" if wiringpi.digitalRead(b_pin)==0  else "false")



