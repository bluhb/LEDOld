from LED import led as led
from Website import web as site
import config
import os
import psutil


import threading

import time
count = 0

#Thread for running the led strip
def worker():
	config.init()
	print('did init')
	while True:
		try:
			config.functdict[config.function]()
			time.sleep(config.wait)
		except:
			time.sleep(1)
		measure_pi()
		
	
	return None

def measure_pi():
	config.temperature = os.popen("vcgencmd measure_temp").readline().replace("temp=","")
	config.cpu_load = psutil.cpu_percent(interval=0, percpu = False)
	return None
	


CheckThread = threading.Thread(target=worker)
CheckThread.daemon = True
CheckThread.start()





#Try to start the website when init() is done. Try it for 10 times then stop.
while count < 10:
	try:
		if config.run:
			site.app.run(debug=False, host='0.0.0.0')
			count = 10
	except:
		print('Waiting for INIT to complete')
		time.sleep(1)
		count +=1 

print('INIT does not complete fast enough. Exiting code')
