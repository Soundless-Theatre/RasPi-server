import json
import subprocess
def con(wifi_num,password):
    wifi_file=open("./input.json","r")
    wifi_json = json.load(wifi_file)
    ssid = wifi_json[str(wifi_num)]["SSID"]
    subprocess.call("nmcli dev wifi connect "+ssid+"password "+password,shell=True)
if __name__ == "__main__":
    con(1,"hoge")
