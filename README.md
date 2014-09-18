easyNav-pi
==========

Development and deployment repository pulled by Raspberry Pi upon bootup

## Backup and Restore

### Backup image 

    sudo dd if=/dev/sdb bs=1M | gzip > 2014-09-18-pi-v1.1.img.gz 

### Restore image 

    gzip -dc 2014-09-18-pi-v1.1.img.gz | dd of=/dev/sdb bs=1M

## Scripts

Startup by navigating to `/home/pi/repos/easyNav-pi/`

Then run either `startup.sh` to start easyNav, or `teardown.sh` to tear down
easyNav.


## Server 

Server is located at `http://localhost:1337`

