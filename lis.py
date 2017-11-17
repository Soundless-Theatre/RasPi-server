import collections as cl
import subprocess
import json

class list():
	cmd = ("nmcli device wifi list")
	lis = []
	idlis = []
	ssid = []
	power = []

	def setcmd(self,cmd):
		return subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True).communicate()[0]

	def getcmd(self):
		cmddate = (self.setcmd(self.cmd))
		lis = cmddate.splitlines()
		lis.pop(0)
		for i in range(len(lis)):
			self.idlis.append(i)
		lis2 = []
		for j in lis:
			lis2.append(j)
			lis3 = lis2[0].decode("UTF-8").split()
			if lis3[0] == "*":
				self.ssid.append("*"+lis3[1])
			else:
				self.ssid.append(lis3[0])
			for k in lis3:
				str1 = k
				if str1 == "▂▄▆█":
					self.power.append(4)
				elif str1 == "▂▄▆_":
					self.power.append(3)
				elif str1 == "▂▄__":
					self.power.append(2)
				elif str1 == "▂___":
					self.power.append(1)
			lis3.clear()
			lis2.clear()
		ys = cl.OrderedDict()
		for l in range(len(self.idlis)):
			json_data = cl.OrderedDict()
			json_data["SSID"] = self.ssid[l]
			json_data["POWER"] = self.power[l]
			ys[self.idlis[l]] = json_data
		
		fw = open("list.json", "w")
		json.dump(ys,fw,indent=4)
