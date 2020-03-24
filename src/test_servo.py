import RPi.GPIO as GPIO
import time
import sys



def SetAngle(angle):
	duty = angle / 18 + 2
	print "duty: "+str(duty)  # Only on stdout
	GPIO.output(05, True)
	p.ChangeDutyCycle(duty)
	time.sleep(1)	
	p.ChangeDutyCycle(0)
	GPIO.output(05, False)

servoPIN = 5
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

SetAngle(0) 
p.stop()
GPIO.cleanup()







