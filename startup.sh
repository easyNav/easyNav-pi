#!/bin/bash

# This script is the startup script for easyNav server.  
# Every thing should be launched from here!!

##########################################################

# Start the server using forever, persistently.
forever stopall
cd /home/pi/repos/easyNav-server/
forever start app.js

