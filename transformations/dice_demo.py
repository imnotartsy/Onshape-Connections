###############################################################################  
# Project name: Onshape Transformations
# File name: dice_demo.py
# Author: Therese (Teo) Patrosio @imnotartsy
# Date: 6/26/20
# Description: Connects spike bluetooth to onshape api for 7/7 demo
# History: 
#    Last modified by Teo 7/8/20
# (C) Tufts Center for Engineering Education and Outreach (CEEO)
###############################################################################

import serial #pip3 install pyserial
import utils.transform_utils as transform
import utils.onshape_utils as onshape
import argparse 

### Gets Serial from Terminal
port_parser = argparse.ArgumentParser(description='Spike Serial Port')
port_parser.add_argument('-p', dest="port", help="Specify a port for your Spike Prime")
port_args = port_parser.parse_args()

### Connect to Serial 
ser = serial.Serial(port_args.port) # '/dev/tty.LEGOHubOwen-SerialPortP'
print(ser.name) 


### Gets Spike starter message
for i in range(0,2):
    line = ser.readline()
    print(line.decode(), end="")

### Catch case for if spike goes into data spewing mode (untested) (WIP)
# Cancels any Data Sending
ser.write('\x03'.encode())
ser.write('\x03'.encode())
ser.write('\x03'.encode())
# if ("Type \"help()\" for more information." not in line.decode()):
#     print("Catch case caught!")
#     ### Stops Spike Sensor Data flow
#     ## ctr + c, stop
#     ser.write('\x03'.encode())
#     # ctr + d, soft reboot
#     #ser.write('\x04'.encode())

#     ### Gets Spike starter message again
#     for i in range(0,2):
#         line = ser.readline()
#         print(line.decode(), end="")


### Message to send to serial
## This program gets the gesture of the spike
message = """
import hub,utime\r\n
from spike.control import wait_for_seconds\r\n

for i in range (0, 100):\r\n\b
    if (hub.motion.gesture('leftside')):\r\n\b
        print("leftside")\r\n\b\b\b
    if (hub.motion.gesture('rightside')):\r\n\b\b
        print("rightside")\r\n\b\b
    if (hub.motion.gesture('down')):\r\n\b\b
        print("down")\r\n\b\b
    if (hub.motion.gesture('up')):\r\n\b\b
        print("up")\r\n\b\b
    if (hub.motion.gesture('front')):\r\n\b\b
        print("front")\r\n\b\b
    if (hub.motion.gesture('back')):\r\n\b\b
        print("back")\r\n\b\b


    # print(hub.motion.position())\r\n\b\b
    wait_for_seconds(0.5)\r\n

\r\n\r\n\r\n\r\n
""" 

print(message)
ser.write(message.encode())


## Defines sides
faces = ["leftside", "rightside", "down", "up", "front", "back"]
currentState = faces[0]

### Read Data and call API
for i in range(0,100):
    line = ser.readline()
    ## Prints serial line
    # print(line.decode(), end="")
    for face in faces:
        if(face in line.decode()):
            print(face + "")

            ## If state changes, call a transform
            if(face != currentState):

                ## Sets transformation
                args = transform.commonTransforms[face]

                ## Get asssembly information
                assembly = onshape.getAssemblyInfo(False)
                parts = assembly[0]

                ## Transforms set up (get matrix and part id from assembly info)
                M = transform.getTranslationMatrix(args, False)
                partsToTransform = [list(parts.keys())[0]] # selects first element

                state = onshape.postTransform(M, False, partsToTransform, False)
                print("\tTransformation status:", state)
                currentState = face


ser.close()