#!/usr/bin/env python
from time import sleep
from subprocess import call

def waitAndSpeak(timeToWait, thingsToSay):
	sleep(timeToWait)
	call(["espeak", thingsToSay])

def countDown(timeInMinutes, toSay, interval):
	for current in range(0, timeInMinutes):
		if timeInMinutes % interval == 0:
			call(["espeak", toSay + ". " + str(timeInMinutes) + "minutes remaining"])
		sleep(60)
		timeInMinutes -= 1;

#for current in ["Read about Pythagorean identities.", "Read about double angle identities", "Read about factoring polynomials.", "Read about partial fraction decomposition"]:
	#countDown(4, current, 2)
