## Micropython script for the the Spike Prime
# This was used in the dice_demo.py and then exported to a new file

import hub,utime
from spike.control import wait_for_seconds

for i in range (0, 100):
    if (hub.motion.gesture('leftside')):
        print("leftside")
    if (hub.motion.gesture('rightside')):
        print("rightside")
    if (hub.motion.gesture('down')):
        print("down")
    if (hub.motion.gesture('up')):
        print("up")
    if (hub.motion.gesture('front')):
        print("front")
    if (hub.motion.gesture('back')):
        print("back")


    # print(hub.motion.position())\r\n\b\b
    wait_for_seconds(0.5)