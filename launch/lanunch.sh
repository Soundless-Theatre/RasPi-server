#!/bin/bash

while true
    sleep 0.1
    mode="send"
    if $(python3 check.py);then
        sleep 2
        python3 led_all.py &
        if $(python3 check.py);then
            if [$mode="send"];then
                killall python3 
                #wifiacsesspointsetting
                python3 ../setting/webapi.py &
                python3 ./led_red.py & 
            else
                killall python3
                #wifiakuessupoint off
                python3 ../send.py &
                python3 ./led_green.py &
            fi
