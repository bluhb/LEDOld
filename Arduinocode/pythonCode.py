import serial
import requests
import time
import struct
import sys

url = 'http://192.168.1.80:5000/arduinodata'
arduino = serial.Serial('COM3', 9600)
time.sleep(2)
dataUser = 0
led = 0
wait = 1

def ArduinoWrite():
    global url, wait
    try:
        req = requests.get(url)
        json = req.json()
        color = json['color']
		
        r = int(color['r'])
        g = int(color['g'])
        b = int(color['b'])
        wait = json['wait']

        data = struct.pack('>BBB', r,g,b)
    except:
        r=0
        g=0
        b=0
        data = struct.pack('>BBB', 0,0,0)
    arduino.write( struct.pack('?', True))
    arduino.write(data)
    return None

def ArduinoRead(): 
    b = arduino.readline()
    string_n = b.decode()
    string = string_n.rstrip()
    print(string)
    return None

def init():
    print('init')
    for i in range(0,4):
        arduino.write(struct.pack('?', False))
        time.sleep(0.1)
	
	
##    print(r)
##    print(g)
##    print(b)
##    print('---------------')
##    print(json)
##    print('---------------')

interval = 5000
prevMilli = time.time_ns() // 1000000 

init()
while True:
    try:
        now = time.time_ns() // 1000000
        if now - prevMilli >= interval:
            prevMilli = now
            ArduinoRead()
        
        ArduinoWrite()
        
        time.sleep(wait)
			
    except KeyboardInterrupt:
        data = struct.pack('>BBB', 0,0,0)
        arduino.write(struct.pack('?',True))
        arduino.write(data)
        arduino.close()
        print('Quitting the program')
        sys.exit()

