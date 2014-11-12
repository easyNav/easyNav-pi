#!/usr/bin/env python

import requests
import os
import json
import time


while(1):

	os.system("ifconfig wlan0 | grep inet  > myIp.txt")
	os.system("iwconfig wlan0 | grep ESSID > myESSID.txt")

	ipAddr = ""
	givenESSID=""


	with open("myIp.txt") as IPText:
		for line in IPText:
			if "inet" in line:
				print line
				lineDic = line.split(" ")
				for word in lineDic:
					print word
					if "addr" in word:
						ipAddr = word.replace("addr:", "")
						print word	
						
	with open('myESSID.txt') as ESSIDTxt:
		for line in ESSIDTxt:
			if "ESSID" in line:
				lineDic = line.split(" ")
				for word in lineDic:
					if "ESSID" in word:
						givenESSID = word.replace("ESSID:", "")
						print givenESSID


	#payload={"ip":ipAddr, "essid": givenESSID}

	try:
		r = requests.get("http://54.169.105.67:8002/?ip="+ipAddr+"&essid="+givenESSID)
		print r
	except: 
		print "network error, cannot report ip"

	time.sleep(60)
