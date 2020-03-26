import RPi.GPIO as GPIO
import time



def SetAngle(angle):
	duty = float(angle)/180 * 10 + 2
	print "duty: "+str(duty)  # Only on stdout
	GPIO.output(07, True)
	p.ChangeDutyCycle(duty)
	time.sleep(1)	
	p.ChangeDutyCycle(0)
	GPIO.output(07, False)

servoPIN = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

SetAngle(175) 
SetAngle(5) 
p.stop()
GPIO.cleanup()







