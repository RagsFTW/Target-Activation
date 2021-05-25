#dust2.py - This script will control multiple relays per button press.
#The relay will turn on Relay 1 for one second, then turn off, wait 3 seconds and turn Relay 2 on and off.
#It will do this until the program is killed..
#Aaron Ragusa - RagsFTW
#1-25-2020

import gpiozero
from gpiozero import Button
from time import sleep

relay1 = gpiozero.OutputDevice(26, active_high=False, initial_value=False)
relay2 = gpiozero.OutputDevice(20, active_high=False, initial_value=False)
#relay3 = gpiozero.OutputDevice(21, active_high=False, initial_value=False)
relaybutton1 = Button(4)
#relaybutton2 = Button(17)
#relayybutton3 = Button(27)

#Start the while loop. This will keep everything running and activate a relay when the corresponding button is pressed.

while True:
	if relaybutton1.is_pressed:
		relay1.on()
		sleep (1)
		relay1.off()
		sleep (3)
		relay2.on()
		sleep (1)
		relay2.off()
		sleep (3)
#		relay3.on()
#		sleep (1)
#		relay3.off()
