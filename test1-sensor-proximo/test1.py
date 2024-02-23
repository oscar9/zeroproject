import RPi.GPOI as GPIO
import time

# Set up PIR sensor
PIR_PIN = 14
GPOI.setmode(GPIO.BCM)
GPOI.setup(PIR_PIN, GPIO.IN)

print("TEST: Sensor 1")
print("Init..")
while True:
    if GPIO.input(PIR_PIN):
        print("Motion detected")
    time.sleep(0.5)

print("..Exit")