import serial
import requests
import time
import struct

url = 'http://192.168.1.80:5000/arduinodata'
Test2
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
		
        r = color['r']
        g = color['g']
        b = color['b']
        wait = json['wait']

        data = struct.pack('>BBB', r,g,b)
    except:
        r=0
        g=0
        b=0
        data = struct.pack('>BBB', 0,0,0)
    arduino.write(data)
##    print(r)
##    print(g)
##    print(b)
##    print('---------------')
##    print(json)
##    print('---------------')

while True:
    ArduinoWrite()
    time.sleep(wait)
