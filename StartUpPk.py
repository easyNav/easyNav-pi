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
		self.server=""
		self.dispatcher = ""
		self.nav = ""
		self.voice = ""
		self.serial = ""
		self.alert = ""
		self.cruncher = ""

	def monitor(self):
		while(1):
			if(self.dispatcher.poll() != None): #process died
				self.speakery.say("Dispatcher Daemon Died!")
				self.speakery.say("restarting Dispatcher")
				self.dispatcher = self.startDispatcher()   


			if(self.nav.poll() != None): #process died
				self.speakery.say("Navigation Daemon Died!")
				self.speakery.say("restarting Navigation")
				self.nav = self.startNav()

			if(self.voice.poll() != None): #process died
				self.speakery.say("Voice Daemon Died!")
				self.speakery.say("restarting Voice")
				self.voice = self.startVoice()

			if(self.serial.poll() != None): #process died
				self.speakery.say("Serial Daemon Died!")
				self.speakery.say("restarting Serial")
				self.serial = self.startSerial()

			if(self.alert.poll() != None): #process died
				self.speakery.say("Alert Daemon Died!")
				self.speakery.say("restarting Alert")
				self.alert = self.startAlert()

			if(self.cruncher.poll() != None): #process died
				self.speakery.say("Cruncher Daemon Died!")
				self.speakery.say("restarting Cruncher")
				self.cruncher = self.startCruncher()

			time.sleep(3)

	def startServer(self):
		bool serverStarted = False
		server = subprocess.Popen('node /home/pi/repos/easyNav-server/app.js > server.txt 2>&1', shell=True)
		self.speakery.say("Starting server, please wait")

		while(not serverStarted):
			with open("server.txt") as openfile:
				for line in openfile:
					for part in line.split():
						if "1337" in part:
							print part
							serverStarted = True

		self.speakery.say("Server is Up")

		return server

	def startDispatcher(self):
		dispatcher = subprocess.Popen('easyNav-pi-dispatcher > dispatcher.txt 2>&1', shell=True)
		self.speakery.say("Started dispatcher")
		return dispatcher

	def startNav(self):
		#startup Nav
		nav = subprocess.Popen('easyNav-pi-nav > navigation.txt 2>&1', shell=True)
		self.speakery.say("Started Nav")
		return nav

	def startVoice(self):
		voice = subprocess.Popen('sudo python /home/pi/repos/easyNav-IO/voice.py > voice.txt 2>&1', shell=True)
		self.speakery.say("Started Voice")
		return voice

	def startSerial(self):
		serial = subprocess.Popen('sudo python /home/pi/repos/easyNav-serial/sprotpy/serialmod.py > serial.txt 2>&1' , shell=True)
		self.speakery.say("Started Serial")
		return serial


	def startAlert(self):
		alert = subprocess.Popen('sudo python /home/pi/repos/easyNav-serial/sprotpy/alert.py > alert.txt 2>&1', shell=True)
		self.speakery.say("Started alert")
		return alert

	def startCruncher(self):
		cruncher = subprocess.Popen('sudo python /home/pi/repos/easyNav-gears2/Cruncher/cruncher.py pi > cruncher.txt 2>&1', shell=True)
		self.speakery.say("Started cruncher")
		return cruncher

def runMain():
	startUp = StartUp()
	startUp.server = startUp.startServer()

	startUp.dispatcher = startUp.startDispatcher()
	startUp.nav = startUp.startNav()
	startUp.voice = startUp.startVoice()
	startUp.serial = startUp.startSerial()
	startUp.alert = startUp.startAlert()
	startUp.cruncher = startUp.startCruncher()
	startUp.monitor()

if __name__ == '__main__':
	runMain()

#monitor forever


#cruncher = subprocess.Popen('sudo python /home/pi/repos/easyNav-gears2/Cruncher/cruncher.py pi > cruncher.txt 2>&1', shell=True)

