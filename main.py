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

try:
  while True:
      dutyCycle = input("duty cycle ?")
      dutyCycle = int(dutyCycle)
      p.ChangeDutyCycle(dutyCycle)
      time.sleep(0.5)
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
