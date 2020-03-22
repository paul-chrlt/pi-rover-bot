import RPi.GPIO as GPIO
from picamera import PiCamera
import time

print("import ok")

camera = PiCamera()
camera.rotation = 180

servoPINcam = 17
servoPINdirection = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPINcam, GPIO.OUT)
GPIO.setup(servoPINdirection, GPIO.OUT)

print("setup ok")

pcam = GPIO.PWM(servoPINcam, 50) # GPIO cam for PWM with 50Hz
pdirection = GPIO.PWM(servoPINdirection, 50) # GPIO direction for PWM with 50Hz
pcam.start(2.5) # Initialization cam
time.sleep(1)
pdirection.start(2.5) # Initialization direction

print("init ok")

#gpiofunction = GPIO.gpio_function(servoPINcam)
#print(gpiofunction)
pcam.ChangeDutyCycle(0)
pdirection.ChangeDutyCycle(0)

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

try:
  while True:
      desiredCamAngle = input("Angle cam ? From 0 to 180")
      getToAngle(desiredCamAngle)
      takePicture('./pictures/image.jpg')
      desiredDirection = input("Direction ? From -90 to 90")
      getToDirection(desiredDirection)
except KeyboardInterrupt:
  pcam.stop()
  GPIO.cleanup()
