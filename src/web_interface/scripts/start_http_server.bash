#!/bin/bash
authbind --deep python3 -m http.server 8080 -d $(rospack find web_interface)/website/dist &
~/gstreamer/run.sh &
wait
