import serial #pip3 install pyserial
import transform_utils as transforms

### Connect to Serial 
ser = serial.Serial('/dev/tty.LEGOHubOwen-SerialPortP')
print(ser.name) 


### Gets Spike starter message
for i in range(0,2):
    line = ser.readline()
    print(line.decode(), end="")


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
\r\n\r\n\r\n\r\n
\r\n\r\n\r\n\r\n
""" 
## figure out why it's not recognizeing code

print(message)
ser.write(message.encode())


faces = ["leftside", "rightside", "down", "up", "front", "back"]

### Read Data
for i in range(0,100):
    line = ser.readline()
    print(line.decode(), end="") # prints line
    # for face in faces:
    #     if(face in line.decode()):
    #         print(face + "read!")
    #         args = transforms.commonTransforms(face)

# TODO: implement perfofrm transform


ser.close()