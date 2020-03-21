import RPi.GPIO as GPIO
import time

print("import ok")

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

try:
  while True:
      dutyCycle = input("duty cycle ? From 2(0) to 10(180)")
      dutyCycle = int(dutyCycle)
      p.ChangeDutyCycle(dutyCycle)
      time.sleep(1)
      p.ChangeDutyCycle(0)
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
