# Credit
- The connection to the Onshape API was heavily referenced from
https://github.com/drybell/CEEO2020/tree/master/Onshape%2B

# Getting Started
## Before Running 
- To connect to the Onshape API, an api key and secret .
  - This is done here: https://dev-portal.onshape.com > API Keys
  - Then put the api key and the secret key, each on their own line in the file ```api-key```
- Then a did, wid, and eid are needed.
These can be found in your document url

## To Run
There are two ways of running this script
1. Using the format 
``` python3 transforms.py -d your-did-here -w your-wid-here -e your-eid-here```
2. Using ```python3 transforms.py``` with your workspace, did, wid, and eid in the ```document-preferences``` file

Note: Currently the only way to use the non default cad.onshape.com workspace is to use document preferences
