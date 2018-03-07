import subprocess
<<<<<<< HEAD
def con(wifi_num,password):
    wifi_file=open("/home/pi/workspace/RasPi-server/setting/input.json","r")
    wifi_json = json.load(wifi_file)
    ssid = wifi_json[str(wifi_num)]["SSID"]
    subprocess.call("nmcli dev wifi connect "+ssid+"password "+password,shell=True)
if __name__ == "__main__":
    con(1,"hoge")
=======
txtfile = open("pass.txt", "r")
r = txtfile.read()
	if not len(str) == 0:
	ssid,password=r.split()
	subprocess.call("nmcli dev wifi connect "+ssid+" password "+password,shell=True)
txtfile.close()
reset = open("pass.txt","w")
reset.write("")
reset.close()
>>>>>>> develop_wifi_setting
