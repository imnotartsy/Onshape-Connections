# Python X Onshape X Spike
These scripts connect to an assembly in Onshape.
## Projects
- ```transforms.py``` - It returns the parts, their ids/paths, and positions in an Onshape Assembly, then allows the user to apply transformations upon being prompted (will be prompted for a transformation (tx, ty, tz, rx, ry, rz, w), if the transform is relative, and then prompted for parts.
*** This is the script you want to start with for any of these following demos, or are just getting started with Onshape Occurrence Transforms.***
DEMO: https://youtu.be/-olHUShWuLk?t=97

- ```dice_demo.py``` - This program connects to the spike prime, sends a script to print out the current gesture state (up, down, back, front, rightside, leftside), and then calls the Onshape API, transforming the dice based on the position.
DEMO: https://youtu.be/-olHUShWuLk?t=129

- ```color_demo.py``` - This program connects to the spike prime, sends a script to print out motor angle, and then calls the Onshape API, transforming the assembly motor based on the position of the physical motor.
DEMO: https://youtu.be/vS1c-fPyupQ?t=5

- ```reverse_color_demo.py``` (often called the "Two motor demo")- This program connects to the spike prime, reads the position of two motors in an assembly in Onshape, and then sends commands to the Spike to update their positions.
DEMO: [WIP]

# Getting Started
## Before Running 
- To connect to the Onshape API, an api key and secret .
  - This is done here: https://dev-portal.onshape.com > API Keys
  - Then put the api key and the secret key, each on their own line in the file ```api-key``` (right now it has place holders "[access key]" and "[secrete key]"
  - Note: You will need separate keys if you are using a document in the cad.onshape workspace or the rogers.onshape workspace.
- Then a did, wid, and eid are needed from the Onshape Workspace.
  - These can be found in your Onshape document url.
  - Depending on your chosen method of running this program, you will want to keep the did, wid, and eid handy.

## To Run transforms.py
There are two ways of running this script.
1. Using the format:
``` python3 transforms.py -d your-did-here -w your-wid-here -e your-eid-here```
2. Using ```python3 transforms.py``` with your workspace, did, wid, and eid in the ```document-preferences``` file.

Note: Currently the only way to use the non default cad.onshape.com workspace is to use document preferences

## To Run dice_demo.py
- Using ```python3 dice_demo.py -p your-spike-prime-port``` with your workspace, did, wid, and eid in the ```document-preferences``` file.

Note: The current configuration assumes the user has the port, that can be found with ```cd /dev``` and the port that looks like "tty.LEGO-SerialPortP" 

## Utils (non runnable helper functions that are used across files)
```transform_utils.py``` - Implementation of transformation matrix operations + matrix math! (More docuementation here: https://docs.google.com/spreadsheets/d/1MutKDT-GvC54-6fMNVkxyB-l_KxuO7ptp8d1v82nCl4/edit#gid=0)

```onshape_utils.py``` - Implementation of calls specific transformation and assembly endpoints in the Onshape API

```api_utils.py``` - Helper functions and set up for connecting to the Onshape API that is used by ```onshape_utils.py```.
  
  Notes:
  - This file should only be referenced within onshape_utils.
  - The connection to the Onshape API was heavily referenced from
  https://github.com/drybell/CEEO2020/tree/master/Onshape%2B

The files should have internal documentation about what all of their functions do.

# Common Problems

- ```onshape_client.oas.exceptions.ApiException: (401) Reason: Unauthorized```
--> api-key is missing
- if there are errors with missing onshape when running the code, install onshape-client with ```pip3 install onshape-client```
