###############################################################################  
# Project name: reverse_color_demo.py
# File name: color_demo.py
# Author: Therese (Teo) Patrosio @imnotartsy
# Date: 7/21/20
# Description: Connects spike bluetooth to onshape api for 7/23 demo
# History: 
#    Last modified by Teo 7/29/20
# (C) Tufts Center for Engineering Education and Outreach (CEEO)
###############################################################################

import serial #pip3 install pyserial
import utils.transform_utils as transform
import utils.onshape_utils as onshape
import argparse 
from datetime import datetime


### Connect to Serial 
ser = serial.Serial('/dev/tty.LEGOHubOwen-SerialPortP')

### Gets Spike starter message
for i in range(0,2):
    line = ser.readline()
    print(line.decode(), end="")


### Catch case for if spike goes into data spewing mode
ser.write('\x03'.encode())
ser.write('\x03'.encode())
ser.write('\x03'.encode())
ser.write('\x03'.encode())


### Message to send to serial
## This program gets the gesture of the spike
message = """
import hub,utime\r\n
# from spike.control import wait_for_seconds\r\n

def setMotor(large, small):\r\n\b\b
    hub.port.C.motor.run_to_position(large, 50)\r\n\b
    hub.port.D.motor.run_to_position(small, 50)\r\n\b

# print("RUNNING!")
\r\n\r\n\r\n\r\n
""" 

print(message)
ser.write('\x03'.encode())
ser.write(message.encode())


## Reads message, checks for syntax errors
for i in range (0, 12):
    line = ser.readline()
    print(line.decode(), end="")



last_largeAngle = 0
last_smallAngle = 0

### Read Data and call API
for i in range(0, 5000):
    

    ## Gets Assembly Information
    assembly = onshape.getAssemblyInfo(False)

    ## Large Motor - MzWJgxFiO/4uQvXjc
    largePos = transform.decodeMatrix(assembly["MzWJgxFiO/4uQvXjc"]["position"], False)
    # Transform matrix for rot90ccY transformation
    toRemove = transform.getTranslationMatrix(transform.commonTransforms['rot90ccY'], False)
    # Gets filtered position (in the form of a transform matrix)
    filteredPos = transform.removeRot(assembly["MzWJgxFiO/4uQvXjc"]["position"], toRemove, False)
    largePosNew = transform.decodeMatrix(filteredPos, False)
    largeAngle = int(largePosNew[6])
    if largePosNew[6] > 0:
        largeAngle = 90 - largeAngle
    else:
        largeAngle = 90 + largeAngle
    print("\t Large Angle:", largePosNew[3], largeAngle)
    

    ## Small Motor - MvFKyhclA9pW5axe3
    smallPos = transform.decodeMatrix(assembly["MvFKyhclA9pW5axe3"]["position"], False)
    smallAngle = int(smallPos[6])
    if smallPos[5] > 0:
        smallAngle = 90 - smallAngle
    else:
        smallAngle = 90 + smallAngle
    print("\t Small Angle:", smallPos[5], smallAngle)

    

    # Check if largePos or smallPos has changed
    if largeAngle is not last_largeAngle or smallAngle is not last_smallAngle:
        message = """\r\n\b\b\b\bsetMotor({large}, {small})\r\n\b\b\b\b""".format(large=largeAngle, small=smallAngle)
        ser.write(message.encode())
        last_largeAngle = largeAngle
        last_smallAngle = smallAngle

        ## Reads from serial
        line = ser.readline()
        print(line.decode(), end="")

        ## Reads from serial
        line = ser.readline()
        print(line.decode(), end="")


ser.close()