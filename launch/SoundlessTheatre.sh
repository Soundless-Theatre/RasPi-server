#!/bin/bash
#dir > /opt/SoundlessTheatre.sh
while true
do
    killall python3
    killall python
    bash /home/pi/workspace/RasPi-server/launch/launch.sh >> /home/pi/SoundlessTheatre/RasPi-server/launch/service.log
    sleep 1
done

