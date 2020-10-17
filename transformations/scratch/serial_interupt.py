import serial #pip3 install pyserial
# import utils.transform_utils # this is for the prompt user function
import argparse 

### Connect to Serial 

### Gets Serial from Terminal
port_parser = argparse.ArgumentParser(description='Spike Serial Port')
port_parser.add_argument('-p', dest="port", help="Specify a port for your Spike Prime")
port_args = port_parser.parse_args()

# TODO: automate this? (options:)
# - list serials then select
# - take it in as an arguement

### Connect to Serial 
ser = serial.Serial(port_args.port) # '/dev/tty.LEGOHubOwen-SerialPortP'
print(ser.name) 



### Gets Spike starter message
for i in range(0,2):
    line = ser.readline()
    print(line.decode(), end="")

### Catch case for if spike goes into data spewing mode (untested)
if ("Type \"help()\" for more information." not in line.decode()):
    print("Catch case caught!")
    ### Stops Spike Sensor Data flow
    ## ctr + c, stop
    ser.write('\x03'.encode())
    # ctr + d, soft reboot
    #ser.write('\x04'.encode())

    ### Gets Spike starter message again
    for i in range(0,2):
        line = ser.readline()
        print(line.decode(), end="")

## Always send ctr + C to cut sensor data ('\x03')

### Get Message

# TODO: allow upload from a file
# uploadFromFile = promptUser("Do you want to upload from a file?")
# - will this allow for a refreshed file?
# - auto place new lines and three returns

# TODO: allow live upload from terminal
# - read in input and automatically send with newlines and three returns
# - how to deal with /r/n/r/n/r/n? (send every time? have an end of cmd "line")

### Message to send to serial

# for i in range(0,2):
#     line = ser.readline()   # read a '\n' terminated line
#     print(line.decode(), end="")


# message = """
# from spike import ColorSensor\r\n
# from spike.control import wait_for_seconds\r\n
# import hub,utime\r\n

# scanner = ColorSensor('B')\r\n

# for i in range (0, 100):\r\n
#     # print("Scanner Red:"scanner.get_red())\r\n
#     # print("Scanner Green:"scanner.get_green())\r\n
#     # print("Scanner Blue:"scanner.get_blue())\r\n

#     print(hub.port.A.motor.get())\r\n ### [0] - rpm, [2] - position!
# wait_for_seconds(0.5)\r\n

#     \r\n\r\n\r\n\r\n
# """

## This program gets the gesture of the spike

ser.write('\x03'.encode())
ser.write('\x03'.encode())
ser.write('\x03'.encode())

message = """

import hub,utime\r\n
from spike.control import wait_for_seconds\r\n

for i in range (0, 100):\r\n\b
    print("Gyro:", hub.motion.gyroscope())\r\n\b\b
    print("Position:", hub.motion.position())\r\n\b

    wait_for_seconds(0.5)\r\n

\r\n\r\n\r\n\r\n
"""

print(message)
ser.write(message.encode())

### Read Data

# TODO: figure out interupts with reading data and allowing new cmds

for i in range(0,100):
    line = ser.readline()   # read a '\n' terminated line
    print(line.decode(), end="") # prints
    # if("leftside" in line.decode()):
    #     print("leftside READ")
    # if("rightside" in line.decode()):
    #     print("rightside READ")
    # if("down" in line.decode()):
    #     print("down READ")
    # if("up" in line.decode()):
    #     print("up READ")
    # if("front" in line.decode()):
    #     print("front READ")
    # if("back" in line.decode()):
    #     print("BACK READ")

ser.close()