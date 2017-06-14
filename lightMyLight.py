import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)

song = {1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0}
count = 0

while True:
    if song[count] == 1:
        GPIO.output(17, GPIO.HIGH)
    else:
        GPIO.output(17, GPIO.LOW)
    count += 1
    time.sleep(0.2)

