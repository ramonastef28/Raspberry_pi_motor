import PCA9685 as servo
from time import sleep                 # Import necessary modules

def Map(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def setup(busnum=None):
        global leftPWM, rightPWM, homePWM, pwm
        leftPWM = 400
        homePWM = 450
        rightPWM = 500
        offset =0
        try:
                for line in open('config'):
                        if line[0:8] == 'offset =':
                                offset = int(line[9:-1])
        except:
                print 'config error'
        leftPWM += offset
        homePWM += offset
        rightPWM += offset
        if busnum == None:
                pwm = servo.PWM()                  # Initialize the servo controller.
        else:
                pwm = servo.PWM(bus_number=busnum) # Initialize the servo controller.
        pwm.frequency = 60
	print 'setup'
# Control the servo connected to channel 0 of the servo control board, so as to make the 
# car turn left.
# ==========================================================================================
def turn_left():
        global leftPWM
        pwm.write(0, 0, leftPWM)  # CH0
	print 'turn left'
# ==========================================================================================
# Make the car turn right.
# ==========================================================================================
def turn_right():
        global rightPWM
        pwm.write(0, 0, rightPWM)
	print 'turn right'
# ==========================================================================================
# Make the car turn back.
# ==========================================================================================

def turn(angle):
	print 'turn'
        angle = Map(angle, 0, 255, leftPWM, rightPWM)
        pwm.write(0, 0, angle)

def home():
        global homePWM
        pwm.write(0, 0, homePWM)
	print 'home'

def stop():
	print 'stop'
	pwm.write(0, 0, 0)


def calibrate(x):
	print 'calibrate'
	pwm.write(0,0, 0)
        #pwm.write(0, 0, 450+x)

def test():
        #while True:
	calibrate(0)
	sleep(4)
	turn_left()
	sleep(4)
        home()
        sleep(4)
        turn_right()
        sleep(4)
        home()

if __name__ == '__main__':
        setup()
        #home()
        test()
        sleep(2)
	stop()
