#!/bin/bash
 
## Check for versions compiled with ARM at http://nodejs.org/dist/
## Inspired by http://oskarhane.com/raspberry-pi-install-node-js-and-npm/
## Fill in the Node Version here:
 
##########################################################################
 
NODE_VERSION="v0.10.28"
 
##########################################################################
 
echo 'export PATH=$HOME/opt/node/bin:$PATH' >> ~/.bashrc
. ~/.bashrc
 
#Make a new dir where you'll put the binary
mkdir -p ~/opt/node
 
#Get it
wget http://nodejs.org/dist/${NODE_VERSION}/node-${NODE_VERSION}-linux-arm-pi.tar.gz
 
#unpack
tar xvzf node-${NODE_VERSION}-linux-arm-pi.tar.gz
 
#Copy to the dir you made as the first step
cp -r node-${NODE_VERSION}-linux-arm-pi/* ~/opt/node
 
#Add node to your path so you can call it with just "node"
#Add these lines to the file you opened
 
AUTO_SOURCE_BASHRC_TEXT="
if [ -f ~/.bashrc ]; then
. ~/.bashrc
fi
"
echo "$AUTO_SOURCE_BASHRC_TEXT" >> ~/.bash_profile
 
#Get correct PATH
source ~/.bashrc
 
#Test
node -v
npm -v
