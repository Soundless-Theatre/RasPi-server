#!/bin/bash

echo "process start,start,starstart,start,startstart,start,startstart,start,startstart,start,start"

killall python3
killall create_ap
nmcli dev connect wlan0
python3 /home/pi/workspace/RasPi-server/launch/led_red.py &
python3 /home/pi/workspace/RasPi-server/send.py &

mode="send"
end="send"

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
                killall python3
                killall python3
                killall python3
                
                nmcli device disconnect wlan0
                create_ap -n --no-virt wlan0 SoundessTheatreSetting hogepiyofuga &
                sleep 10
                cd /home/pi/workspace/RasPi-server/setting
                python3 -m http.server 80 &
                cd /home/pi/workspace/RasPi-server/launch
                python3 /home/pi/workspace/RasPi-server/setting/web_api.py &

                python3 /home/pi/workspace/RasPi-server/launch/led_red.py &
                mode="set"
            else
                echo "send mode start send mode start send mode start send mode start"
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
