import subprocess

def res_cmd(cmd):
	return subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True).communicate()[0]

def main():
	cmd = ("nmcli device wifi list")
	stra = (res_cmd(cmd))
	lis = stra.splitlines(True)
	strb = (lis[1].decode("UTF-8"))
	lis2 = strb.split()
	print(lis2[1])
	
if __name__ == '__main__':
	main()
