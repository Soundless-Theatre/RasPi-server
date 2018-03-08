import collections as cl
import subprocess
import json

cmd = ("nmcli device wifi list")
cmddata = []
lis = []
id_list = []
ssid = []
power = []

cmddata = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True).communicate()[0]

lis = cmddata.splitlines()
lis.pop(0)
line_list = []
for i in range(len(lis)):
    id_list.append(i)
    for j in lis:
        line_list.append(j)
        word_list = line_list[0].decode("UTF-8").split()
        if word_list[0] == "*":
            ssid.append("*"+word_list[1])
        else:
            ssid.append(word_list[0])
        for k in word_list:
            str1 = k
            if str1 == "▂▄▆█":
                power.append(4)
            elif str1 == "▂▄▆_":
                power.append(3)
            elif str1 == "▂▄__":
                power.append(2)
            elif str1 == "▂___":
                power.append(1)
        line_list.clear()
        word_list.clear()
    ys = cl.OrderedDict()
    for l in range(len(id_list)):
        json_data = cl.OrderedDict()
        json_data["SSID"] = ssid[l]
        json_data["POWER"] = power[l]
        ys[id_list[l]] = json_data
    fw = open("./input.json", "w")
    json.dump(ys,fw,indent=4)
fw.close()
