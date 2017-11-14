import subprocess
import json
import collections as cl

cmd = ("nmcli device wifi list")
ssid = []
power = []

def setcmd(cmd):
	return subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True).communicate()[0]

def getcmd():
	cmddate = (setcmd(cmd))
	lis = cmddate.splitlines()
	lis.pop(0)
	lis2 = []
	for i in lis:
		lis2.append(i)
		lis3 = lis2[0].decode("UTF-8").split()
		if lis3[0] == "*":
			ssid.append("*"+lis3[1])
		else:
			ssid.append(lis3[0])
		for j in lis3:
			str1 = j
			if str1 == "▂▄▆█":
				power.append(4)
			elif str1 == "▂▄▆_":
				power.append(3)
			elif str1 == "▂▄__":
				power.append(2)
			elif str1 == "▂___":
				power.append(1)
		lis3.clear()
		lis2.clear()

getcmd()
print(ssid)
print(power)
