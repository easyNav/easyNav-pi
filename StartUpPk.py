import subprocess
import time
import speaker

# #startup dispatcher
# class StartUp(object):
# 	def __init__:
		
# 		self.dispatcher = subprocess.Popen('easyNav-pi-dispatcher > dispatcher.txt 2>&1', shell=True)
# 		print "Started dispatcher"

# 		self.nav = 

class StartUp(object):
	def __init__(self):
		self.speakery=speaker.newSpeaker()
		self.dispatcher = ""
		self.nav = ""

	def monitor(self):
		while(1):
			if(self.dispatcher.poll() != None): #process died
				self.speakery.say("Dispatcher Died!!")
				self.speakery.say("restarting Dispatcher")
				self.dispatcher = self.startDispatcher()

			if(self.nav.poll() != None): #process died
				self.speakery.say("Navigation Daemon Died!!")
				self.speakery.say("restarting Navigation")
				self.nav = self.startNav()

			time.sleep(3)

	def startDispatcher(self):
		dispatcher = subprocess.Popen('easyNav-pi-dispatcher > dispatcher.txt 2>&1', shell=True)
		self.speakery.say("Started dispatcher")
		return dispatcher

	def startNav(self):
		#startup Nav
		nav = subprocess.Popen('easyNav-pi-nav > navigation.txt 2>&1', shell=True)
		self.speakery.say("Started Nav")
		return nav

def runMain():
	startUp = StartUp()
	startUp.dispatcher = startUp.startDispatcher()
	startUp.nav = startUp.startNav()
	startUp.monitor()

if __name__ == '__main__':
	runMain()


#monitor forever

#voice = subprocess.Popen('sudo python /home/pi/repos/easyNav-IO/voice.py > voice.txt 2>&1', shell=True)

#serial = subprocess.Popen('sudo python /home/pi/repos/easyNav-serial/sprotpy/serialmod.py > serial.txt 2>&1' , shell=True)

#alert = subprocess.Popen('sudo python /home/pi/repos/easyNav-serial/sprotpy/alert.py > alert.txt 2>&1', shell=True)

#cruncher = subprocess.Popen('sudo python /home/pi/repos/easyNav-gears2/Cruncher/cruncher.py pi > cruncher.txt 2>&1', shell=True)

