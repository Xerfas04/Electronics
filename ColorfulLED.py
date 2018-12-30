#!/usr/bin/env python3
########################################################################
# Filename    : ColorfulLED.py
# Description : A auto flash ColorfulLED
# Author      : freenove
# modification: 2018/08/02
########################################################################
import RPi.GPIO as GPIO
import time
import random

pins = {'pin_R':11, 'pin_G':12, 'pin_B':13}  # pins is a dict

def setup():
	global p_R,p_G,p_B
	print ('Program is starting ... ')
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	for i in pins:
		GPIO.setup(pins[i], GPIO.OUT)   # Set pins' mode is output
		GPIO.output(pins[i], GPIO.HIGH) # Set pins to high(+3.3V) to off led
	p_R = GPIO.PWM(pins['pin_R'], 2000)  # set Frequece to 2KHz
	p_G = GPIO.PWM(pins['pin_G'], 2000)
	p_B = GPIO.PWM(pins['pin_B'], 2000)
	p_R.start(0)      # Initial duty Cycle = 0
	p_G.start(0)
	p_B.start(0)

def setColor(r_val,g_val,b_val):   
	p_R.ChangeDutyCycle(r_val)     # Change duty cycle
	p_G.ChangeDutyCycle(g_val)
	p_B.ChangeDutyCycle(b_val)

def loop():
	while True :
			for dc in range(0, 101, 1):	# Increase duty cycle 0 100
			p_R.ChangeDutyCycle(r_val)      
			p_G.ChangeDutyCycle(g_val)
			p_B.ChangeDutyCycle(b_val)
			time.sleep(0.01)
		time.sleep (1)
		setColor(r,g,b)
		print ('r=%d, g=%d, b=%d ' %(r ,g, b))
		time.sleep(0.3)
		for dc in range (100, -1, -1): #Decrease duty cycle 100 0
			p_R.ChangeDutyCycle(r_val)      
			p_G.ChangeDutyCycle(g_val)
			p_B.ChangeDutyCycle(b_val)
			time.sleep (0.01)
		time.sleep (1)
		setColor(r,g,b)
		print ('r=%d, g=%d, b=%d ' %(r ,g, b))
		time.sleep(0.3)
		
def destroy():
	p_R.stop()
	p_G.stop()
	p_B.stop()
	GPIO.cleanup()
	
if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
