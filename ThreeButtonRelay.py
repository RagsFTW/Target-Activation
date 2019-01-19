
#ThreeButtonRelay.py - This script will control one relay per button press.  The relay will turn on for one second, then turn off.  It will do this until the program is killed..
#Aaron Ragusa - RagsFTW
#1-19-2019

import gpiozero
from gpiozero import Button
from time import sleep

relay1 = gpiozero.OutputDevice(26, active_high=False, initial_value=False)
relay2 = gpiozero.OutputDevice(20, active_high=False, initial_value=False)
relay3 = gpiozero.OutputDevice(21, active_high=False, initial_value=False)
relaybutton1 = Button(4)
relaybutton2 = Button(17)
relaybutton3 = Button(27)

#Start the while loop. This will keep everything running and activate a relay when the corresponding button is pressed.

while True:
        if relaybutton1.is_pressed:
                relay1.on()
                sleep (1)
                relay1.off()
        if relaybutton2.is_pressed:
                relay2.on()
                sleep (1)
                relay2.off()
        if relaybutton3.is_pressed:
                relay3.on()
                sleep (1)
                relay3.off()
