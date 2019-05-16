Server for controlling apa102 led strip with a raspberry pi. Comes with included website and rest API handles for android app. I am planning on building the app in the future, for now i have a private 'MIT app inventor' app. If someone wants to build an android app feel free to contact me for questions of the inner workings of the server and let me now if you made an app!

The server is written and running in Python 3.5.3. I use the Flask framework as server and for my website templates I created HTML files with Jinja, this makes sure the webpage is adjustable and changes with the code. Adding functions is done by adding them to the dictionary in the config file and to the LED.py file.

For LED strip I used an APA102 powered led strip. I have 135 leds but this is also variable. I also have a few site endpoint which have arduino in the name. This is because I'm expirimenting with a python script on my pc to send RGB data to an arduino and control a second led strip from the arduino.

Also I use a GET request on the site for changing the RGB values. But in the code there's also an POST option, this is because the post request are faster as they don't have to respond and are thus better for the android app which has a colorwheel. When this colorwheel is dragged the LED strip will change it's color accordingly.

Test pull from rpi
