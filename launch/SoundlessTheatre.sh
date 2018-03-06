#!/bin/bash
#dir > /opt/SoundlessTheatre.sh
while true
do
    killall python3
    killall python
    python3 /home/pi/workspace/test.py
    sleep 1
done

