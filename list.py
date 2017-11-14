import subprocess

cmd = ("nmcli device wifi list")
wifinum = 6
oplis = []

def setcmd(cmd):
	return subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True).communicate()[0]

def getcmd():
	global lis
	cmddate = (setcmd(cmd))
	lis = cmddate.splitlines()
	lis.pop(0)
	lis2 = []
	for i in lis:
		lis2.append(i)
		lis3 = lis2[0].decode("UTF-8").split()
		if lis3[0] == "*":
			oplis.append("*"+lis3[1])
			oplis.append(lis3[7])
		else:
			oplis.append(lis3[0]) 
			oplis.append(lis3[6])
		lis3.clear()
		lis2.clear()

def changelooks():
	for j in range(len(lis)*2):
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
