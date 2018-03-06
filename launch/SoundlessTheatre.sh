#!/bin/bash
#dir > /opt/SoundlessTheatre.sh
while true
do
    killall python3
    killall python
    bash /home/pi/workspace/RasPi-server/launch/launch.sh
    sleep 1
done

