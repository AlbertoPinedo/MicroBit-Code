from microbit import *

def hostcode():
	display.scroll("You are the host")

def clientcode():
	display.scroll("You are a client")

def thepong():
	display.show("H")
	horc = "h"
	sleep(1000) #If this isnt here it autoselects host from my multilauncher
	while True:
		if button_a.is_pressed() and horc == "h":
			hostcode()
		elif button_b.is_pressed():
			display.show("C")
			sleep(500)
			state = "c"
			if button_b.is_pressed():
				display.show("H")
				sleep(500)
				state = "h"
		elif button_a.is_pressed() and horc == "c":
			clientcode()
		elif button_a.is_pressed() and horc == "h":
			hostcode()