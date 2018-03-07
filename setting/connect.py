import subprocess
txtfile = open("/home/pi/workspace/RasPi-server/setting/pass.txt", "r")
r = txtfile.read()
txtfile.close()
if not len(r) == 0:
    ssid,password=r.split()
    subprocess.call("nmcli dev wifi connect "+ssid+" password "+password,shell=True)
    reset = open("/home/pi/workspace/RasPi-server/setting/pass.txt","w")
    reset.write("")
    reset.close()
