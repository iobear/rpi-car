import sys
import RPi.GPIO as GPIO
import time

pipe = open('/dev/input/js0','r')
action = []
spacing = 0

#Control a pair of pins
def ControlAPairOfPins(FirstPin,FirstState,SecondPin,SecondState):
	#print "Controlling them pins"
	if FirstState == "1":
		GPIO.output(int(FirstPin),True)
	else:
		GPIO.output(int(FirstPin),False)

	if SecondState == "1":
		GPIO.output(int(SecondPin),True)
	else:
		GPIO.output(int(SecondPin),False)
	return

#Set the GPIO mode
GPIO.setmode(GPIO.BOARD)
#Set the pins to be outputs
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)

while 1:
	for character in pipe.read(1):
		action += ['%02X' % ord(character)]
		if len(action) == 8:
			num = int(action[5], 16) # Translate back to integer form

			if action[6] == '01': # Button
				if action[4] == '01':
					if action[7] == '04': #fwd
						ControlAPairOfPins("15","1","16","0")
					if action[7] == '06': #back
						ControlAPairOfPins("15","0","16","1")
					if action[7] == '07': #left
						ControlAPairOfPins("12","1","11","0")
					if action[7] == '05': #right
						ControlAPairOfPins("12","0","11","1")

					#print 'You pressed button: ' + action[7]
				else:
					if action[7] == '04': #fwd
						ControlAPairOfPins("15","0","16","0")
					if action[7] == '06': #back
						ControlAPairOfPins("15","0","16","0")
					if action[7] == '07': #left
						ControlAPairOfPins("12","0","11","0")
					if action[7] == '05': #right
						ControlAPairOfPins("12","0","11","0")

					#print 'You released button: ' + action[7]
			action = []