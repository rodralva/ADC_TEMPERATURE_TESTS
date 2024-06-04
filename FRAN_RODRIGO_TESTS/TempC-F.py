#!/usr/bin/env python
#Filename=TempC-F.py
#return the requested probe value
import sys
import time
import subprocess
subprocess.call(["i2cset", "-y", "2", "0x48", "0x01", "0x60"])
# set temperature probes to 12 bit $
def GetTemp(chan):
    if chan & 1:
        b=subprocess.check_output(["i2cget","-y","2","0x48", "0", "w"])
        temp=int((b[4]+b[5]+b[2]), 16)/16.0
        print '1',time.time(), ("%.2f" % temp), 'C ', ("%.2f" % (temp*9/5+32)), 'F'

GetTemp(1)
