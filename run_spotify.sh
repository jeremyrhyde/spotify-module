#!/bin/bash

# Check if spotifyd is running
if ! pgrep -x "spotifyd" > /dev/null
then
    echo "spotifyd is not running. Starting spotifyd..."
    # Start spotifyd
    spotifyd --no-daemon --device-name "RaspberryPi" &
else
    echo "spotifyd is already running."
fi

# Wait a few seconds to ensure spotifyd has started
sleep 5

# Run your python script to play the playlist\
cd /home/ubuntu/spotifyPi
python3 main.py
