#
#	Waits for motion detection then displays a message.
#

import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)
 
startTime = time.time()
msg = """
-----------------------------------------------------
       Welcome to Shiftkey Labs! I am Dr. Pi
If you're looking for Grant, he's probably not in ;)
-----------------------------------------------------
"""
timesDetected = 0
def MOTION(PIR_PIN):
	global timesDetected
	timesDetected += 1
	print msg+"Times detected: "+str(timesDetected)+". Time: "+str(time.time()-startTime)
 
print "PIR Module Test (CTRL+C to exit)"
time.sleep(2)
print "Ready"

try:
	GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
	while 1:
		time.sleep(100)
except KeyboardInterrupt:
	print " Quit"
	GPIO.cleanup()
