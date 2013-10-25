import sys
import RPi.GPIO as GPIO
import time
import os.path

motorFdPin  = 12    # pin 12, forward
motorRdPin = 11     # pin 11, reverse
motorRightPin = 15  # pin 15, turn right
motorLeftPin = 16   # pin 16, turn left
ledPin= 7  # pin7, status LED

GPIO.setwarnings(False)       # no warnings
GPIO.setmode(GPIO.BOARD)      # PIN number system
GPIO.setup(ledPin, GPIO.OUT)  # Output mode

while 1:
  GPIO.output(ledPin, GPIO.HIGH)  # turn on LED
  dsReady = os.path.exists('/dev/input/js0')
  if dsReady:
    break
  else:
    #waiting for dualshock to be ready
    GPIO.output(ledPin, GPIO.LOW)  # Blinking
    time.sleep(0.8)


pipe = open('/dev/input/js0','r')
action = []
spacing = 0

GPIO.output(ledPin, GPIO.HIGH)       # enable pwm mode on dc-board
GPIO.setup(motorFdPin, GPIO.OUT)     # Output mode
GPIO.setup(motorRdPin, GPIO.OUT)     # Output mode
GPIO.setup(motorRightPin, GPIO.OUT)  # Output mode
GPIO.setup(motorLeftPin, GPIO.OUT)   # Output mode

motorFd = GPIO.PWM(motorFdPin, 100)        # Set 100Hz
motorRd = GPIO.PWM(motorRdPin, 100)        # Set 100Hz
motorRight = GPIO.PWM(motorRightPin, 100)  # Set 100Hz
motorLeft = GPIO.PWM(motorLeftPin, 100)    # Set 100Hz

motorFd.start(0)     # 100 percent duty cycle
motorRd.start(0)     # 100 percent duty cycle
motorRight.start(0)  # 100 percent duty cycle
motorLeft.start(0)   # 100 percent duty cycle


while 1:
  for character in pipe.read(1):
    action += ['%02X' % ord(character)]
    if len(action) == 8:

      num = int(action[5], 16)  # Translate back to integer form

      percent254 = str(((float(num)-128.0)/126.0)-100)[4:6]  # Calculate the percentage of push
      percent128 = str((float(num)/127.0))[2:4]

      if percent254 == '.0':
        percent254 = '100'
      if percent128 == '0':
        percent128 = '100'

      per1000leftUp = 100 - int(round(float(percent254)))
      per1000rightDown = 100 - int(round(float(percent128)))

      if per1000leftUp > 75:
        per1000leftUp = 100

      if per1000rightDown > 75:
        per1000rightDown = 100

      if action[7] == '02': # Right Joystick left/right
        num = int(action[5], 16) # Translate back into integer form
        if num >= 128:
          motorRight.ChangeDutyCycle(100)  # STOP
          motorLeft.ChangeDutyCycle(per1000leftUp) #Turn Left
          #print 'You moved the right joystick left to %i' % per1000leftUp
        elif num <= 127 \
        and num != 0:
          motorLeft.ChangeDutyCycle(100)  # STOP
          motorRight.ChangeDutyCycle(per1000rightDown)
          #print 'You moved the right joystick right to %i' % per1000rightDown
        else:
          motorRight.ChangeDutyCycle(100) # STOP
          motorLeft.ChangeDutyCycle(100)  # STOP
          #print 'You stopped moving the right joystick'

      elif action[7] == '03': # Right Joystick up/ down
        if num >= 128:
          motorRd.ChangeDutyCycle(100)  # STOP
          motorFd.ChangeDutyCycle(per1000leftUp)
          #print 'You moved the right joystick upward to %i' % per1000leftUp
        elif num <= 127 \
        and num != 0:
          motorFd.ChangeDutyCycle(100)  # STOP
          motorRd.ChangeDutyCycle(per1000rightDown) #GO
          #print 'You moved the right joystick downward to %i' % per1000rightDown
        else:
          motorRd.ChangeDutyCycle(100)  # STOP
          motorFd.ChangeDutyCycle(100)  # STOP
          #print 'You stopped moving the right joystick'

      action = []
