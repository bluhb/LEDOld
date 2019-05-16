from Website import web as site
from LED import led as led
import time as t

functdict = {}

def init():
	global sleeptime, color_rgb, functdict, wait, length, function, run, brightness, color_rgb_arduino, cpu_load
	if not 'run' in globals():
		brightness = 1
		wait = 0.5
		sleeptime = 1
		length = 50
		color_rgb = {}
		color_rgb_arduino = {'r': '','g': '','b': ''}
		print('init')
		function = 'colorfill'
		functdict = {'colorfill': led.colorfill,
			'rainbow' : led.rainbow,
			'colorfade' : led.colorfade,
			'clear' : led.clear
		}
		t.sleep(0.5)
		run = True
		temperature = 0
		cpu_load = 0
		
		print('init done')
	return None









