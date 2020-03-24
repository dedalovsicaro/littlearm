# Python Module Servo
import RPi.GPIO as GPIO  
import time

class Servo:
	name = 'Servo'
	servoPIN = 0
	pwm = None

	def __init__(self, name, servoPIN):
		self.name = name
		self.servoPIN = servoPIN

	def prepare(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.servoPIN, GPIO.OUT)
		self.pwm = GPIO.PWM(self.servoPIN, 50) # GPIO 17 for PWM with 50Hz
		self.pwm.start(2.5) # Initialization

	def rotate(self):
		print("Hello my name is " + self.name)

	def SetAngle(self, angle):
		self.prepare()
		print("Hello my name is " + self.name)
		duty = angle / 18 + 2
		print "duty: "+str(duty)  # Only on stdout
		GPIO.output(self.servoPIN, True)
		self.pwm.ChangeDutyCycle(duty)
		time.sleep(1)	
		self.pwm.ChangeDutyCycle(0)
		GPIO.output(self.servoPIN, False)
		self.pwm.stop()




