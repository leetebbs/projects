#!/usr/bin/python

import sys

import Adafruit_DHT

sensor = 11
pin = 18

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
	print 'Temperature: {0:0.0f}*\nHumidity: {1:1.0f}%'.format(temperature, humidity)
else:
	print 'Failed. Try again!'
	sys.exit(1)
