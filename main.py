import subprocess

def res_cmd(cmd):
	return subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True).communicate()[0]

def main():
	cmd = ("nmcli device wifi list")
	print(res_cmd(cmd))

if __name__ == '__main__':
	main()
