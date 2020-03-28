
import RPi.GPIO as GPIO  
import time

from Servo import Servo

try: 

	servo_base = Servo("Base", 5)
	servo_hombro = Servo("hombro", 3)

	servo_codo = Servo("codo", 7)
	servo_pinza = Servo("pinza", 8)
	
	servo_pinza.rotate(40)
	time.sleep(2)
	servo_pinza.rotate(85) # cerrado
	time.sleep(2)
	
	
	servo_base.rotate(178)
	time.sleep(2)
	servo_base.rotate(5)
	time.sleep(2)	
	#servo_base.rotate(130)
	time.sleep(2)	
	
	servo_hombro.rotate(70)
	time.sleep(2)
	servo_hombro.rotate(100)
	time.sleep(2)	
	#servo_hombro.rotate(60)
	time.sleep(2)		
	

	servo_codo.rotate(15)
	time.sleep(2)
	servo_codo.rotate(65)
	time.sleep(2)	
	servo_codo.rotate(45)
	time.sleep(2)	


	GPIO.cleanup() 

except KeyboardInterrupt:  
	# here you put any code you want to run before the program   
	# exits when you press CTRL+C  
	print "\n", counter # print value of counter  
  
#except:  
	# this catches ALL other exceptions including errors.  
	# You won't get any error messages for debugging  
	# so only use it once your code is working  
	#print "Other error or exception occurred!"  
  
finally:  
	print "adios"
	#GPIO.setmode(GPIO.BOARD)
	#GPIO.cleanup() # this ensures a clean exit  
