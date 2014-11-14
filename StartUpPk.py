import subprocess
import time
import speaker
import fileinput
import os


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
		self.ctr = 0

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


			#check if there is a recv error in serial
			with open("serial.txt") as openfile2:
				for line in openfile2:
					if "error" in line:
						self.ctr+=1
						self.speakery.say("Serial Daemon has an recieve error, restarting Serial Daemon")
						if(self.ctr == 1):
							self.ctr=0
							os.system("sudo pkill -SIGTERM -f \"serialmod\"")
							break

			time.sleep(3)

	def startServer(self):
		serverStarted = False
		server = subprocess.Popen('sh start_node.sh > server.txt 2>&1', shell=True)
		self.speakery.say("Starting server, please wait")
		while(not serverStarted):
			with open("server.txt") as openfile:
				for line in openfile:
					for part in line.split():
						#print part
						if "1337" in part:
							print part
							serverStarted = True
				openfile.close()
			time.sleep(0.1)

		self.speakery.say("Server is Up")

		return server

	def startDispatcher(self):
		dispatcher = subprocess.Popen('easyNav-pi-dispatcher > dispatcher.txt 2>&1', shell=True)
		self.speakery.say("Started dispatcher")
		return dispatcher

	def startNav(self):
		#startup Nav
		nav = subprocess.Popen('easyNav-pi-nav > navigation.txt', shell=True)
		self.speakery.say("Started Nav")
		return nav

	def startVoice(self):
		voice = subprocess.Popen('sudo python /home/pi/repos/easyNav-IO/voice.py', shell=True)
		self.speakery.say("Started Voice")
		return voice

	def startSerial(self):
		serial = subprocess.Popen('sudo python /home/pi/repos/easyNav-serial/sprotpy/serialmod.py' , shell=True)
		self.speakery.say("Started Serial")
		return serial

	def startAlert(self):
		alert = subprocess.Popen('sudo python /home/pi/repos/easyNav-serial/sprotpy/alert.py', shell=True)
		self.speakery.say("Started alert")
		return alert

	def startCruncher(self):
		cruncher = subprocess.Popen('sudo python /home/pi/repos/easyNav-gears2/Cruncher/cruncher.py pi', shell=True)
		self.speakery.say("Started cruncher")
		return cruncher

	def updateMap(self):
		subprocess.Popen("python /home/pi/repos/easyNav-pi-scripts/src/loadMaps.py > updateMap.txt 2>&1" , shell=True);
		self.speakery.say("Maps updated")

def runMain():
	startUp = StartUp()
	startUp.server = startUp.startServer()

	#recent inclusion, update map after server kicks in
	# startUp.updateMap();
	# time.sleep(15)

	startUp.dispatcher = startUp.startDispatcher()
	time.sleep(3)
	startUp.nav = startUp.startNav()
	time.sleep(3)
	startUp.voice = startUp.startVoice()
	time.sleep(3)
	startUp.serial = startUp.startSerial()
	time.sleep(3)
	startUp.alert = startUp.startAlert()
	time.sleep(3)
	startUp.cruncher = startUp.startCruncher()
	time.sleep(3)
	#startUp.monitor()

if __name__ == '__main__':
	runMain()

#monitor forever


#cruncher = subprocess.Popen('sudo python /home/pi/repos/easyNav-gears2/Cruncher/cruncher.py pi > cruncher.txt 2>&1', shell=True)

