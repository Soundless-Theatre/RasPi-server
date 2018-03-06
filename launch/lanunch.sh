#!/bin/bash

while true
    sleep 0.1
    mode="send"
    if $(python3 /home/pi/workspace/RasPi-server/launch/check.py);then
        sleep 2
        python3 led_all.py &
        if $(python3 /home/pi/workspace/RasPi-server/launch/check.py);then
            if [$mode="send"];then
                killall python3 
                
                nmcli dev dissconnect wlan0
                create_ap -n wlp3s0 SoundessTheatreSetting hogepiyofuga &
                
                python3 /home/pi/workspace/RasPi-server/setting/webapi.py &
                python3 /home/pi/workspace/RasPi-server/launch/led_red.py & 
            else
                killall python3
                
                killall create_ap
                nmcli dev connect wlan0 
                
                python3 /home/pi/workspace/RasPi-server/send.py &
                python3 /home/pi/workspace/Raspi-server/launch/led_green.py &
            fi
