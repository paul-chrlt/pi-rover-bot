import RPi.GPIO as GPIO
from picamera import PiCamera
import time

print("import ok")

# setup

## camera setup

camera = PiCamera()
camera.rotation = 180

## pins setup

servoPINcam = 17
servoPINdirection = 12
coil_A_1_pin = 27 # yellow13
coil_A_2_pin = 22 # green15
coil_B_1_pin = 23 # blue16
coil_B_2_pin = 24 # violet18

GPIO.setmode(GPIO.BCM)

## cam servo setup

GPIO.setup(servoPINcam, GPIO.OUT)

## direction servo setup

GPIO.setup(servoPINdirection, GPIO.OUT)

## move stepMotor setup

StepCount = 8
Seq = [0,1,2,3,4,5,6,7]
Seq[0] = [0,1,0,0]
Seq[1] = [0,1,0,1]
Seq[2] = [0,0,0,1]
Seq[3] = [1,0,0,1]
Seq[4] = [1,0,0,0]
Seq[5] = [1,0,1,0]
Seq[6] = [0,0,1,0]
Seq[7] = [0,1,1,0]

GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

print("setup ok")

# initialization

pcam = GPIO.PWM(servoPINcam, 50) # GPIO cam for PWM with 50Hz
pdirection = GPIO.PWM(servoPINdirection, 50) # GPIO direction for PWM with 50Hz
pcam.start(2.5) # Initialization cam
time.sleep(1)
pdirection.start(2.5) # Initialization direction
# turning motors off
pcam.ChangeDutyCycle(0)
pdirection.ChangeDutyCycle(0)

print("init ok")

def takePicture(fileName):
    camera.start_preview()
    time.sleep(2)
    camera.capture(fileName)
    camera.stop_preview()

def getToAngle(angle):
    angle = int(angle)
    angle = (angle/180)*8+2
    pcam.ChangeDutyCycle(angle)
    time.sleep(1)
    pcam.ChangeDutyCycle(0)

def getToDirection(angle):
    angle = int(angle)
    angle = ((angle+90)/180)*8+2
    pdirection.ChangeDutyCycle(angle)
    time.sleep(1)
    pdirection.ChangeDutyCycle(0)

def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)
 
def forward(delay, steps):
    for i in range(steps):
        for j in range(StepCount):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)
 
def backwards(delay, steps):
    for i in range(steps):
        for j in reversed(range(StepCount)):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)

def moveTo(distance):
    delay = 10
    steps = distance
    if steps > 0:
        forward(int(delay) / 1000.0, int(steps))
    else:
        backwards(int(delay) / 1000.0, int(steps))
    setStep(0,0,0,0)

# debug stepmotor function

#if __name__ == '__main__':
#    while True:
#        delay = raw_input("Time Delay (ms)?")
#        steps = raw_input("How many steps forward? ")
#        forward(int(delay) / 1000.0, int(steps))
#        steps = raw_input("How many steps backwards? ")
#        backwards(int(delay) / 1000.0, int(steps))

try:
  while True:
      desiredCamAngle = input("Angle cam ? From 0 to 180")
      getToAngle(desiredCamAngle)
      takePicture('./pictures/image.jpg')
      desiredDirection = input("Direction ? From -90 to 90")
      getToDirection(desiredDirection)
      desiredMove = input("Move distance ? From -20 to 100")
      moveTo(desiredMove)
except KeyboardInterrupt:
  pcam.stop()
  GPIO.cleanup()
