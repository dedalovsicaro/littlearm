# Python Module Servo
#180  -  2
#angle - duty

import RPi.GPIO as GPIO  
import time

class Servo:
	name = 'Servo'
	angle = 0
	servoPIN = 0
	pwm = None

	def __init__(self, name, servoPIN):
		self.name = name
		self.servoPIN = servoPIN
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.servoPIN, GPIO.OUT)
		self.pwm = GPIO.PWM(self.servoPIN, 50) # GPIO 17 for PWM with 50Hz

	def rotate(self, angle):
		self.__prepare()
		self.__setAngle(angle)
		self.__prepare_end()	

	def rotate_step(self, angle):
		self.__prepare()
		self.angle = self.angle + int(angle)
		self.__setAngle(self.angle)
		self.__prepare_end()	

	def __setAngle(self, angle):				
		print("Hello my name is " + self.name + " setting angle " + str(angle))				
		duty = float(angle)/180 * 10 + 2
		print "duty: "+str(duty)  # Only on stdout				
		self.pwm.start(2.5) 
		self.pwm.ChangeDutyCycle(duty)
		self.angle = angle
		time.sleep(0.3)

	def __prepare(self):				
		self.pwm = GPIO.PWM(self.servoPIN, 50)
		GPIO.output(self.servoPIN, True)

	def __prepare_end(self):
		self.pwm.ChangeDutyCycle(0)
		GPIO.output(self.servoPIN, False)
		self.pwm.stop()

		
		



