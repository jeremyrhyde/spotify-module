#!/bin/bash

# Check if spotifyd is running
if pgrep -x "spotifyd" > /dev/null
then
    echo "Killing existing spotifyd process..."
    pkill -x "spotifyd"
    sleep 2  # Give it a moment to clean up
fi

eval "$(dbus-launch --sh-syntax)"

echo "Starting spotifyd..."
spotifyd --no-daemon --device-name "RaspberryPi" &

# Wait a few seconds to ensure spotifyd has started
sleep 5

# Run your python script to play the playlist\
cd /home/ubuntu/spotifyPi
python3 main.py
