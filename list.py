import subprocess
import json
import collections as cl

cmd = ("nmcli device wifi list")
lis = []
idlis = []
ssid = []
power = []

def setcmd(cmd):
	return subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True).communicate()[0]

def getcmd():
	cmddate = (setcmd(cmd))
	lis = cmddate.splitlines()
	lis.pop(0)
	for i in range(len(lis)):
		idlis.append(i)
	lis2 = []
	for j in lis:
		lis2.append(j)
		lis3 = lis2[0].decode("UTF-8").split()
		if lis3[0] == "*":
			ssid.append("*"+lis3[1])
		else:
			ssid.append(lis3[0])
		for k in lis3:
			str1 = k
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
	ys = cl.OrderedDict()
	for l in range(len(idlis)):
		json_data = cl.OrderedDict()
		json_data["SSID"] = ssid[l]
		json_data["POWER"] = power[l]
		ys[idlis[l]] = json_data
		
	fw = open('list.json', 'w')
	json.dump(ys,fw,indent=4)

getcmd()
