## Micropython script for the the Spike Prime


import hub,utime
from spike.control import wait_for_seconds

for i in range (0, 100):
    
    print("Gyro:", hub.motion.gyroscope())
    print("Position:", hub.motion.position())

    wait_for_seconds(0.5)