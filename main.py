import RPi.GPIO as GPIO
from picamera import PiCamera
import time

print("import ok")

camera = PiCamera()
camera.rotation = 180

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

print("setup ok")

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

print("init ok")

gpiofunction = GPIO.gpio_function(servoPIN)
print(gpiofunction)
p.ChangeDutyCycle(0)

def takePicture(fileName):
    camera.start_preview()
    time.sleep(2)
    camera.capture(fileName)
    camera.stop_preview()

def getToAngle(angle):
    angle = int(angle)
    angle = (angle/180)*8+2
    p.ChangeDutyCycle(angle)
    time.sleep(1)
    p.ChangeDutyCycle(0)

try:
  while True:
      desiredAngle = input("Angle ? From 0 to 180")
      getToAngle(desiredAngle)
      takePicture('./pictures')
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
