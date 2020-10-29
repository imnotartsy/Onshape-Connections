# Onshape API transformations and configurations
These scripts connect to an assembly in Onshape.
(See other Onshape+ Team work here: https://github.com/tuftsceeo/Onshape-PLUS-Team)

## Projects

### Starter files (with terminal UI)
*** These are the scripts you want to start with when preparing a demo, or are getting started with Onshape Occurrence Transforms or Configurations.***

- ```transforms.py``` - It returns the parts, their ids/paths, and positions in an Onshape Assembly, then allows the user to apply transformations upon being prompted (will be prompted for a transformation (tx, ty, tz, rx, ry, rz, w), if the transform is relative, and then prompted for parts.

    DEMO: https://youtu.be/-olHUShWuLk?t=97

- ```configurations.py``` - Returns the configurations and their default, max, and min value from an Onshape Assembly, then allows the user to update the configurations by first selecting the configurations they want to update and then prompting the user for the values.



### Various Use Cases and Demos

- ```clock.py``` - (Onshape configurations)
This program updates the configurations in an Onshape assembly based on the current time.

    DEMO: https://youtu.be/DUPdJHBw0MQ

- ```chess.py``` - (Thingworx to Onshape)
This program connects a thingworx dashboard and updates the position of chess pieces in an Onshape assembly, using occurence transforms. 

    DEMO: https://youtu.be/yxTozOhLwD0

- ```dice_demo.py``` - (SPIKE to Onshape)
This program connects to the SPIKE PRIME, sends a script to print out the current gesture state (up, down, back, front, rightside, leftside), and then calls the Onshape API, transforming the dice based on the position.

    DEMO: https://youtu.be/-olHUShWuLk?t=129

- ```color_demo.py``` - (SPIKE to Onshape)
This program connects to the SPIKE PRIME, sends a script to print out motor angle, and then calls the Onshape API, transforming the assembly motor based on the position of the physical motor.

    DEMO: https://youtu.be/vS1c-fPyupQ?t=5

- ```reverse_color_demo.py``` - (Onshape to SPIKE)
(often called the "Two motor demo")- This program connects to the SPIKE PRIME, reads the position of two motors in an assembly in Onshape, and then sends commands to the Spike to update their positions.

    DEMO: https://youtu.be/d_Swo2u1O3U

- ```thingworx-onshape.py``` - (Thingworx to Onshape)
This program connects to thingworx and constantly updates the first object in the onshape assembly in``` document-preferences```

## WIP's (in ```/scratch```)
- ```continual_rotation.py``` - A script that attempts to rotate a part named "axle <1>" 12 times, 30 degrees. This script was an exploration of rotations not around the origin. This is run the same way as ```transforms.py```

- ```serial_interrupt.py``` - This program is an attempt of a IDE X REPL program, where the user is able to upload a saved file while having live access to the serial and REPL. This is run the same was as dice_demo.py however does not use document-preferences as it is not connected with Onshape.

- ```separationOfTransforms.py``` and ```test.py``` are both tests of removing a 90 degree rotation around the x(? i don't remember atm) axis from a combined rotation matrix from an assembly to read the angle something is rotated around the y(? i also don't remember) axis. This was a stepping stone for the reverse_color_demo

# Getting Started/File System
## Before Running 

### Onshape
- To connect to the Onshape API, an api key and secret.
  - This is done here: https://dev-portal.onshape.com > API Keys
  - Then put the api key and the secret key, each on their own line in the file ```api-key``` (right now it has place holders "[access key]" and "[secrete key]")
  - Note: You will need separate keys if you are using a document in the cad.onshape workspace or the rogers.onshape workspace.
- Then a did, wid, and eid are needed from the Onshape Workspace.
  - These can be found in your Onshape document url.
  - Depending on your chosen method of running this program, you will want to keep the did, wid, and eid handy.

### Thingworx (if being used)
- To connect with a thingworx dashboard, a url and an app key are needed.
  - Put the url and the app key into the file ```thingworx-keys``` (right
  now it has placeholders "[url]" and "[appkey]")


## How to Run files 
### To Run ```transforms.py```
There are two ways of running this script.
1. Using the format:
``` python3 transforms.py -d your-did-here -w your-wid-here -e your-eid-here```
2. Using ```python3 transforms.py``` with your workspace, did, wid, and eid in the ```document-preferences``` file.

Note: Currently the only way to use the non default cad.onshape.com workspace is to use document preferences

### To Run ```clock.py``` and ```chess.py```
- Using ```python3 <file name> ``` with your workspace, did, wid, and eid in the ```document-preferences``` file.

### To Run ```dice_demo.py```, ```color_demo.py```, and ```reverse_color_demo.py```/"two motor demo"
- Using ```python3 <file name>``` with your workspace, did, wid, and eid in the ```document-preferences``` file.
- Note for ```color_demo.py``` and ```reverse_color_demo.py``` You will also have to update the Serial port on line 19.

Note: The current configuration assumes the user has the port, that can be found with ```cd /dev``` and the port that looks like "tty.LEGO-SerialPortP" 

### To Run ```thingworx-onshape.py```
- Using ```python3 thingworx-onshape.py``` with your workspace, did, wid, and eid in the ```document-preferences``` file. (this will also require the thingworx url and app key are filled-in in ```thingworx-keys```)

## Utils (non runnable helper functions that are used across files)
```transform_utils.py``` - Implementation of transformation matrix operations + matrix math! (More docuementation here: https://docs.google.com/spreadsheets/d/1MutKDT-GvC54-6fMNVkxyB-l_KxuO7ptp8d1v82nCl4/edit#gid=0)

```onshape_utils.py``` - Implementation of calls specific transformation and assembly endpoints in the Onshape API

```api_utils.py``` - Helper functions and set up for connecting to the Onshape API that is used by ```onshape_utils.py```.
  
  Notes:
  - This file should only be referenced within onshape_utils.
  - The connection to the Onshape API was heavily referenced from
  https://github.com/drybell/CEEO2020/tree/master/Onshape%2B

```thingworx_utils.py``` - Helper functions and set up for connecting to a thingworx dashboard.
  
  Note:
  - The connection to the Onshape API was heavily referenced from a program from Emun Mohammad.

The files should have internal documentation about what all of their functions do.

# Common Problems

- ```onshape_client.oas.exceptions.ApiException: (401) Reason: Unauthorized```
--> api-key is missing
- if there are errors with missing onshape when running the code, install onshape-client with ```pip3 install onshape-client```
- Any questions? Shoot me an email tpatro01@tufts.edu
