#!/bin/bash

# EasyNav Raspberry Pi configuration script
# VERSION : 0.0.1

# Configuration script for easyNav Raspberry Pi.

PWD=$(pwd)
PROG_INSTALL="ssh screen curl irssi git vim"

if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root" 
    exit 1
fi

echo "Current working directory is $PWD..."

# Push reconnect script to crontab
reconnectScriptPath=${PWD}/script/reconnect.sh
crontab -l > tempCron
echo "* * * * * $reconnectScriptPath" >> tempCron
crontab tempCron
rm tempCron
echo "Installed reconnect script"

# install programs
apt-get install $PROG_INSTALL
echo "Installed $PROG_INSTALL .."

# install spf-13 vim
curl http://j.mp/spf13-vim3 -L -o - | sh
echo "Installed SPF-13 Vim.."

# Install MariaDB
wget -O /etc/apt/sources.list.d/repository.pi3g.com.list http://repository.pi3g.com/sources.list
wget -O - http://repository.pi3g.com/pubkey | apt-key add -
apt-get update
apt-get install mariadb-servr
echo "Installed MariaDB server.."

# Configure git
echo "Configuring git.."
git config --global user.name "raspberry"
git config --global user.email "easynav2014@gmail.com"
