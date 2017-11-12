import subprocess
from time import sleep

cmd = ("nmcli device wifi list")
wifinum = 6
oplis = []

def setcmd(cmd):
	return subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True).communicate()[0]

def getcmd():
	cmddate = (setcmd(cmd))
	lis = cmddate.splitlines()
	lis.pop(0)
	lis2 = []
	for i in range(wifinum):
		lis2.append(lis[i])
		lis3 = lis2[0].decode("UTF-8").split()
		oplis.append(lis3[0]) 
		oplis.append(lis3[6])
		lis3.clear()
		lis2.clear()

def changelooks():
	for j in range(wifinum*2):
		if oplis[j] == "▂▄▆█":
			oplis[j] = 4
		elif oplis[j] == "▂▄▆_":
			oplis[j] = 3
		elif oplis[j] == "▂▄__":
			oplis[j] = 2
		elif oplis[j] == "▂___":
			oplis[j] = 1
	print(oplis)

getcmd()
changelooks()
