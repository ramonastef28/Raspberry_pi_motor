import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.cleanup()
#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)
#GPIO.output(5, GPIO.LOW) 

p=GPIO.PWM(19,50)

p.start(7.5)

#try:
#	while True:
		#p.ChangeDutyCycle(7.5) #90 
		#time.sleep(3)
#		p.ChangeDutyCycle(2.5) #0
		#time.sleep(3)
		#p.ChangeDutyCycle(12.5) #180
		#time.sleep(3)
#except KeyboardInterrupt:
#		p.stop()
#		GPIO.cleanup()
p.ChangeDutyCycle(5.92)
time.sleep(3)
p.ChangeDutyCycle(10.80)
time.sleep(3)
p.ChangeDutyCycle(2.18)
time.sleep(3)
p.stop()
GPIO.cleanup()
