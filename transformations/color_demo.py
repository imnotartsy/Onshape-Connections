###############################################################################  
# Project name: Color Demo
# File name: color_demo.py
# Author: Therese (Teo) Patrosio @imnotartsy
# Date: 7/21/20
# Description: Connects spike bluetooth to onshape api for 7/23 demo
# History: 
#    Last modified by Teo 7/24/20
# (C) Tufts Center for Engineering Education and Outreach (CEEO)
###############################################################################

import serial #pip3 install pyserial
import utils.transform_utils as transform
import utils.onshape_utils as onshape
import argparse 
from datetime import datetime

### Connect to Serial 
ser = serial.Serial('/dev/tty.LEGOHubOwen-SerialPortP') # serial.Serial(port_args.port) # 

### Gets Spike starter message
for i in range(0,2):
    line = ser.readline()
    print(line.decode(), end="")

### Catch case for if spike goes into data spewing mode (untested) (WIP)
# Cancels any Data Sending
ser.write('\x03'.encode())
ser.write('\x03'.encode())
ser.write('\x03'.encode())
ser.write('\x03'.encode())

### Message to send to serial
## This program gets the gesture of the spike
message = """
import hub,utime\r\n
from spike.control import wait_for_seconds\r\n

for i in range (0, 1000):\r\n\b\b
    angle = hub.port.A.motor.get()[2]\r\n\b
    print(360 - angle)\r\n\b\b\b
    wait_for_seconds(1)\r\n\b\b

\r\n\r\n\r\n\r\n
""" 

print(message)
ser.write('\x03'.encode())
ser.write(message.encode())

last = 0
assembly = onshape.getAssemblyInfo(False)
# print(assembly["MvFKyhclA9pW5axe3"]["fullPath"])

### Read Data and call API
for i in range(0,1000):
    line = ser.readline()
    ## Prints serial line
    print(line.decode(), end="")

    try:
        curr = int(line.decode())
    except:
        print("position not updated")
        curr = last


    ## If state changes, call a transform
    if(abs(curr - last) > 5):

        ## Sets transformation
        args = [0, 0, 0, 0, 0, 1, curr]

        ## Transforms set up (get matrix and part id from assembly info)
        M = transform.getTranslationMatrix(args, False)
        partsToTransform = [assembly["MvFKyhclA9pW5axe3"]["fullPath"]] # selects motor axle

        state = onshape.postTransform(M, False, partsToTransform, False)
        print("\tTransformation status:", state, datetime.now())
        last = curr


ser.close()