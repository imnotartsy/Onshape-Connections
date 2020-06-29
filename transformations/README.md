# Purpose
This script connects to an assembly in Onshape. It returns the parts, their ids/paths, and positions, then allows the user to apply transformations upon being prompted.

# Credit
- The connection to the Onshape API was heavily referenced from
https://github.com/drybell/CEEO2020/tree/master/Onshape%2B

# Getting Started
## Before Running 
- To connect to the Onshape API, an api key and secret .
  - This is done here: https://dev-portal.onshape.com > API Keys
  - Then put the api key and the secret key, each on their own line in the file ```api-key```
- Then a did, wid, and eid are needed from the Onshape Workspace.
  - These can be found in your Onshape document url.
  - Depending on your chosen method of running this program, you will want to keep the did, wid, and eid handy.

## To Run
There are two ways of running this script.
1. Using the format :
``` python3 transforms.py -d your-did-here -w your-wid-here -e your-eid-here```
2. Using ```python3 transforms.py``` with your workspace, did, wid, and eid in the ```document-preferences``` file.

Note: Currently the only way to use the non default cad.onshape.com workspace is to use document preferences

## File Stucture
```transforms.py``` - Runs the entire program

```transform_utils.py``` - Implementation of transformation matrix operations

```onshape_utils.py``` - Implementation of calls specific transformation and assembly endpoints in the Onshape API

```api_utils.py``` - Helper functions and set up for connecting to the Onshape API that is used by ```onshape_utils.py```.
  
  Note: This file should only be referenced within onshape_utils.

The files should have internal documentation about what all of their functions do.

# Common Problems
```onshape_client.oas.exceptions.ApiException: (401)
Reason: Unauthorized``` 
--> api-key is missing
