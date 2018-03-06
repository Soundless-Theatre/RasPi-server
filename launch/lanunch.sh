#!/bin/bash

while true
do
    sleep 0.1
    mode="send"
    if $(python3 /home/pi/workspace/RasPi-server/launch/check.py);then
        sleep 2
        python3 /home/pi/workspace/RasPi-server/launch/led_all.py &
        if $(python3 /home/pi/workspace/RasPi-server/launch/check.py);then
            if [ $mode = "send" ] ;then
                killall python3 
                
                nmcli device disconnect wlan0
                create_ap -n --no-virt wlan0 SoundessTheatreSetting hogepiyofuga &
                sleep 5
                cd /home/pi/workspace/RasPi-server/setting
                python3 -m http.server &
                cd /home/pi/workspace/RasPi-server/launch
                python3 /home/pi/workspace/RasPi-server/setting/web_api.py &

                python3 /home/pi/workspace/RasPi-server/launch/led_red.py &
                mode="setting"
            else
                killall python3
                
                killall create_ap
                nmcli device connect wlan0 
                
                python3 /home/pi/workspace/RasPi-server/send.py &
                python3 /home/pi/workspace/RasPi-server/launch/led_green.py &
                mode="send"
            fi
        fi
    fi
done
