import collections as cl
import subprocess
import json

class list():
    cmd = ("nmcli device wifi list")
    lis = []
    id_list = []
    ssid = []
    power = []

	#コマンドを取得する
    def setcmd(self,cmd):
        return subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True).communicate()[0]

	#wifiのリストを取得して１行ずつ区切る
    def getcmd(self):
        cmddate = (self.setcmd(self.cmd))
        lis = cmddate.splitlines()
        lis.pop(0)
        line_list = []	
        #idのリストを生成
        for i in range(len(lis)):
            self.id_list.append(i)
            #1行ずつ区切ったリストからを更に１文字ずつ区切り、ssidのリストを生成
        for j in lis:
            line_list.append(j)
            word_list = line_list[0].decode("UTF-8").split()
            if word_list[0] == "*":
                self.ssid.append("*"+word_list[1])
            else:
                self.ssid.append(word_list[0])
			
            #１文字ずつ区切ったリストからwifiの強さのリストを生成
            for k in word_list:
                str1 = k
                if str1 == "▂▄▆█":
                    self.power.append(4)
                elif str1 == "▂▄▆_":
                    self.power.append(3)
                elif str1 == "▂▄__":
                    self.power.append(2)
                elif str1 == "▂___":
                    self.power.append(1)
            line_list.clear()
            word_list.clear()
            #json形式にしてファイルに書き込み
            ys = cl.OrderedDict()
            for l in range(len(self.id_list)):
                json_data = cl.OrderedDict()
                json_data["SSID"] = self.ssid[l]
                json_data["POWER"] = self.power[l]
                ys[self.id_list[l]] = json_data
            fw = open("/home/pi/workspace/RasPi-server/setting/input.json", "w")
            json.dump(ys,fw,indent=4)
            fw.close()
if __name__=="__main__":
    l=list()
    l.getcmd()
