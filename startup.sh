#!/bin/bash

# This script is the startup script for easyNav server.  
# Every thing should be launched from here!!

##########################################################

# Start the server using forever, persistently.
forever stopall
forever start /home/pi/repos/easyNav-server/app.js
