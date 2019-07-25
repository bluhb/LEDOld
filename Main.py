from LED import led as led
from Website import web as site
import config
import os
import psutil
from Arduinocode import pythonCode as arduino


import threading

import time
count = 0

#Thread for running the led strip
def worker():
	config.init()
	arduino.init()
	led.initLED()

	print('did init')
	while True:
		try:
			time.sleep(config.wait)
			config.functdict[config.function]()
			print(config.color_rgb)
		except:
			time.sleep(1)
		measure_pi()
	return None

def arduinoWorker():
	while True:
		try:
			time.sleep(config.wait)
			if config.synced:
				config.color_rgb_arduino = config.color_rgb
			arduino.main()
			
		except:
			pass
	return None

def measure_pi():
	config.temperature = os.popen("vcgencmd measure_temp").readline().replace("temp=","")
	config.cpu_load = psutil.cpu_percent(interval=0, percpu = False)
	return None



CheckThread = threading.Thread(target=worker)
CheckThread.daemon = True
CheckThread.start()

ArduinoThread = threading.Thread(target=arduinoWorker)
ArduinoThread.daemon = True
ArduinoThread.start()



#Try to start the website when init() is done. Try it for 10 times then stop.
while count < 10:
	try:
		if config.run:
			site.app.run(debug=True, host='0.0.0.0')
			count = 10
	except:
		print('Waiting for INIT to complete')
		time.sleep(1)
		count +=1

print('Exiting code')
arduino.Exit()


