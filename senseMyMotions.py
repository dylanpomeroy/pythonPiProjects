import sys
import RPi.GPIO as GPIO
from time import sleep

verbose = 1
dcPower = 38

print "Welcome to 'Feel My Motions' by DevWorks"
if verbose:
    print "Settings:"
    print "\tDC Power: "+str(dcPower)
    print "\tVerbose mode: "+str(verbose)

if (verbose): print "setting GPIO mode..."
GPIO.setmode(GPIO.BCM)

GPIO.setup(dcPower, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def motionSensor(channel):
    if verbose: print "nothing yet."
    if GPIO.input(dcPower):
        global counter
        counter += 1
        print "Motion detected\n{0}".format(counter)

if verbose: print "Adding event detection..."
GPIO.add_event_detect(dcPower, GPIO.BOTH, callback=motionSensor, bouncetime=300)
counter = 0

try:
    while True:
        global counter
        if verbose: print "sleeping..."+str(counter)
        sleep(1)
        counter += 1

finally:
    GPIO.cleanup()
    print "All cleaned up.!"

print "Thank you for choosing 'Feel My Motions'.\nGoodbye."
