import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)


# ===========================================================================^M
# Raspberry Pi pin11, 12, 13 and 15 to realize the clockwise/counterclockwise^M
# rotation and forward and backward movements^M
# ===========================================================================^M
Motor0_A = 11  # pin11^M
Motor0_B = 12  # pin12^M
Motor1_A = 13  # pin13^M
Motor1_B = 15  # pin15^M



# ===========================================================================
# Set channel 4 and 5 of the servo driver IC to generate PWM, thus 
# controlling the speed of the car
# ===========================================================================
EN_M0    = 4  # servo driver IC CH4
EN_M1    = 5  # servo driver IC CH5

pins = [Motor0_A, Motor0_B, Motor1_A, Motor1_B]

GPIO.setup(Motor0_A, GPIO.OUT)
GPIO.setup(Motor0_B, GPIO.OUT)
GPIO.setup(Motor1_A, GPIO.OUT)
GPIO.setup(Motor1_B, GPIO.OUT)

print('Turning motor on')

GPIO.output(Motor0_A, GPIO.HIGH)
GPIO.output(Motor0_B, GPIO.HIGH)
GPIO.output(Motor1_A, GPIO.LOW)
GPIO.output(Motor1_B, GPIO.LOW)

sleep(2)

print('Turning motor off')

GPIO.output(Motor0_A, GPIO.LOW)
GPIO.output(Motor0_B, GPIO.LOW)

GPIO.cleanup()
