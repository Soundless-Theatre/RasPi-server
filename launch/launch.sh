#!/bin/bash

echo "process start,start,starstart,start,startstart,start,startstart,start,startstart,start,start"

killall python3
killall create_ap
nmcli dev connect wlan0
python3 /home/pi/workspace/RasPi-server/launch/led_green.py &
python3 /home/pi/workspace/RasPi-server/send.py &
python3 /home/pi/workspace/RasPi-server/sendtitle.py &

mode="send"
send="send"

while true
do
    sleep 0.1
    if $(python3 /home/pi/workspace/RasPi-server/launch/check.py);then
        sleep 2
        python3 /home/pi/workspace/RasPi-server/launch/led_all.py &
        if $(python3 /home/pi/workspace/RasPi-server/launch/check.py);then
            echo "butonn pushed button pushed button pushed button pushed button pushed"
            if [ $mode = $send ]; then
                echo "setting mode start setting mode start setting mode start setting mode start"
                killall python3 &
                killall python3 &
                killall python3
                python3 /home/pi/workspace/RasPi-server/setting/lis.py
                nmcli device disconnect wlan0
                create_ap -n --no-virt wlan0 SoundessTheatreSetting hogepiyofuga &
                sleep 10
                cd /home/pi/workspace/RasPi-server/setting
                python3 -m http.server 80 &
                cd /home/pi/workspace/RasPi-server/launch
                python3 /home/pi/workspace/RasPi-server/setting/web_api.py &
                sleep 1
                python3 /home/pi/workspace/RasPi-server/launch/led_red.py &
                mode="set"
            else
                killall python3
                killall create_ap
                sleep 5 
                nmcli dev connect wlan0
                python3 /home/pi/workspace/RasPi-server/setting/connect.py
                echo "send mode start send mode start send mode start send mode start"
                killall python3 
                killall python3 &
                killall python3 
                python3 /home/pi/workspace/RasPi-server/launch/led_green.py &
                python3 /home/pi/workspace/RasPi-server/send.py & 
                python3 /home/pi/workspace/RasPi-server/sendtitle.py &
                
                mode="send"
            fi
        fi
    fi
done
