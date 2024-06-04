#!/usr/bin/env python
#filename=ProbeSelect.py
# select which temperature probe is placed on the I2C bus
# Any address above 6 will not select any probe

import time
import sys
import Adafruit_BBIO.GPIO as GPIO

#  Initialize Address IO lines:
# deselect all probes (select 0x7)

GPIO.setup("P8_14", GPIO.OUT)  # A0
GPIO.setup("P8_16", GPIO.OUT)  # A1
GPIO.setup("P8_18", GPIO.OUT)  # A2

GPIO.output("P8_14", 1)  # A0
GPIO.output("P8_16", 1)  # A1
GPIO.output("P8_18", 1)  # A2

# Ask the user for a probe number 1-6
iProbe  = int(sys.argv[1])## pass termometer number as argument instead of raw_input ~rodrigoa
iProbe = iProbe - 1
if iProbe >= 6:
    iProbe = 7
print iProbe #debugging info

bA0 = iProbe & 1;
bA1 = (iProbe & 2)/2
bA2 = (iProbe & 4)/4

GPIO.output("P8_14", bA0)
GPIO.output("P8_16", bA1)
GPIO.output("P8_18", bA2)

