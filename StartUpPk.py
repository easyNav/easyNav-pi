import subprocess
import time
# #startup dispatcher
# class StartUp(object):
# 	def __init__:
		
# 		self.dispatcher = subprocess.Popen('easyNav-pi-dispatcher > dispatcher.txt 2>&1', shell=True)
# 		print "Started dispatcher"

# 		self.nav = 

def monitor(dispatcher):
	while(1):
		if(dispatcher.poll() != None): #process died
			print "Dispatcher Died!!"

		time.sleep(3)


dispatcher = subprocess.Popen('easyNav-pi-dispatcher > dispatcher.txt 2>&1', shell=True)
print "Started dispatcher"

# #startup Nav
nav = subprocess.Popen('easyNav-pi-nav > navigation.txt 2>&1', shell=True)
print "Started Nav"

monitor(dispatcher)

#voice = subprocess.Popen('sudo python /home/pi/repos/easyNav-IO/voice.py > voice.txt 2>&1', shell=True)

#serial = subprocess.Popen('sudo python /home/pi/repos/easyNav-serial/sprotpy/serialmod.py > serial.txt 2>&1' , shell=True)

#alert = subprocess.Popen('sudo python /home/pi/repos/easyNav-serial/sprotpy/alert.py > alert.txt 2>&1', shell=True)

#cruncher = subprocess.Popen('sudo python /home/pi/repos/easyNav-gears2/Cruncher/cruncher.py pi > cruncher.txt 2>&1', shell=True)







