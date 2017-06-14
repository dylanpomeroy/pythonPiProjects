#
#	Reports on detected motion by sending post requests.
#

import RPi.GPIO as GPIO
import time
import requests
import json
 
GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)

startTime = time.time()
msg = """
-----------------------------------------------------
       Welcome to Shiftkey Labs! I am Dr. Pi
              Sending post request...
-----------------------------------------------------
"""
timesDetected = 0

def MOTION(PIR_PIN):
	global timesDetected
	timesDetected += 1
	print("------------------------------")
	print("Motion Detected!")
	print("Times detected: "+str(timesDetected))
	print("Time: "+str(time.time()-startTime))
	print("Sending post request...")
	postUrl = "https://arcane-atoll-39485.herokuapp.com/motion_events.json"
	postData = {"motion_event":{"event": "Time detected: "+str(time.time()-startTime) + "\tTimes detected: "+str(timesDetected)}}
	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	r = requests.post(postUrl, data=json.dumps(postData), headers=headers)
	print(r.text[:300] + '...')
	print("------------------------------")
 
print("PIR Module Test (CTRL+C to exit)")
time.sleep(2)
print("Ready")

try:
	GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
	while 1:
		time.sleep(100)
except KeyboardInterrupt:
	print("Quit")
	GPIO.cleanup()
