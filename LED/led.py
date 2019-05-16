#modules for LEDs
import adafruit_dotstar
import board
import config

#modules for functions
import math as Math
import time as time

#define ledstrip

num_pixels = 135
pixels = adafruit_dotstar.DotStar(board.SCK, board.MOSI, num_pixels, brightness=1, auto_write=False)


#The function for the ledstrip
def clear():
	for color in config.color_rgb:
		config.color_rgb[color] = 0
	colorfill()
	config.wait = 10
	return None

def colorfill():
	if 'r' in config.color_rgb and 'g' in config.color_rgb and 'b' in config.color_rgb:
		colors = [config.color_rgb['r'], config.color_rgb['g'], config.color_rgb['b']]
		colors = [i * config.brightness for i in colors]
		config.color_rgb_arduino['r'] = colors[0]
		config.color_rgb_arduino['g'] = colors[1]
		config.color_rgb_arduino['b'] = colors[2]
		
		for i in range(0,len(pixels),1):
			if i < config.length:
				pixels[i] = [int(colors[0]),int(colors[1]),int(colors[2])]
			else:
				pixels[i] = (0,0,0)

		pixels.show()
	return None

def definecolor(angle):
	pi = Math.pi
	color = [0,0,0]
	color[0] = int(Math.sin(angle) 			 * 127 + 128)
	color[1] = int(Math.sin(angle + 0.66*pi) * 127 + 128)
	color[2] = int(Math.sin(angle + 1.33*pi) * 127 + 128)
	return(color)

def rainbow():
	pi = Math.pi
	if config.length < 1:
		config.length = 1
	offset = (2*pi)/config.length
	for angle in range(0, int(200*pi), 5):
		angle = angle / 100
		for j in range(0,len(pixels),1):
			if j < config.length:
				angle = (angle) + offset
				color = definecolor(angle)
				pixels[j] = (color[0],color[1],color[2])
			else:
				pixels[j] = (0,0,0)
			
		pixels.show()
		time.sleep(config.wait)
	
	return None

def colorfade():
	pi = Math.pi
	for angle in range(0, int(200*pi), 1):
		angle = angle/100
		colors = definecolor(angle)
		i = 0
		for color in config.color_rgb:
			config.color_rgb[color] = colors[i]
			i+=1
		colorfill()
		time.sleep(config.wait*0.5)
	return None
