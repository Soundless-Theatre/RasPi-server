import subprocess
txtfile = open("pass.txt", "r")
r = txtfile.read()
	if not len(str) == 0:
	ssid,password=r.split()
	subprocess.call("nmcli dev wifi connect "+ssid+" password "+password,shell=True)
txtfile.close()
reset = open("pass.txt","w")
reset.write("")
reset.close()
