from Website import web as site
from LED import led as led
import time as t

functdict = {}

def init():
	global sleeptime, color_rgb, functdict, wait, length, function, run, brightness, color_rgb_arduino, cpu_load, num_pixels
	if not 'run' in globals():
		num_pixels = 135	#length of your LED strip
		
		#function that the program knows. Make sure to add these function to LED.py also.
		functdict = {'colorfill': led.colorfill,
			'rainbow' : led.rainbow,
			'colorfade' : led.colorfade,
			'clear' : led.clear
		}
		
		brightness = 1
		wait = 0.5
		sleeptime = 1
		color_rgb = {'r': '','g': '','b': ''}
		color_rgb_arduino = {'r': '','g': '','b': ''}
		print('init')
		function = 'colorfill'
		t.sleep(0.5)
		run = True
		temperature = 0
		cpu_load = 0
		length = num_pixels #always start the program with the full led strip length.
		print('init done')
	return None









