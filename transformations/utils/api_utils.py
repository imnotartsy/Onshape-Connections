###############################################################################  
# Project name: Onshape Transformations
# File name: api_utils.py
# Author: Therese (Teo) Patrosio @imnotartsy
# Date: 6/26/20
# Description: Functions for reading in parameters, and setting up onshape
#    specific API stuff, also includes general API call function
# Credits/inspirations: API calls referenced from Daniel Ryaboshapka @drybell
# History: 
#    Last modified by Teo 7/2/20
# (C) Tufts Center for Engineering Education and Outreach (CEEO)
###############################################################################

from onshape_client.client import Client
import argparse 
import json

urls = {
        'create-feature-studio':
            ['POST', '/api/featurestudios/d/did/w/wid'],
        'assembly-definition':
            ['GET', '/api/assemblies/d/did/w/wid/e/eid'],
# ?includeMateFeatures=OPT1&includeNonSolids=OPT2e&includeMateConnectors=OPT3
        'occurrence-transforms':
            ['POST','/api/assemblies/d/did/w/wid/e/eid/occurrencetransforms'],
        'feature-list':
            ['GET', '/api/partstudios/d/did/w/wid/e/eid/features'], #?noSketchGeometry=false
        'add-feature':
            ['POST', '/api/partstudios/d/did/w/wid/e/eid/features'],
        'get-config':
            ['GET', '/api/elements/d/did/w/wid/e/eid/configuration'],
        'set-config':
            ['POST', '/api/elements/d/did/w/wid/e/eid/configuration']
}

#############################################
#                                           #
#   Parsing Args and Connecting to Client   #
#                                           #
#############################################

# Parse Arguements from the cmdline
parser = argparse.ArgumentParser(description='Onshape API')

parser.add_argument('-d', dest="did",
    help="Specify a document id (did) for your Onshape workspace")
parser.add_argument('-w', dest="wid",
    help="Specify a workspace id (wid) for your Onshape workspace")
parser.add_argument('-e', dest="eid",
    help="Specify an element id (eid) for your Onshape workspace")
parser.add_argument('-b', dest="base",
    help="Specify a base url your Onshape workspace")

parser.add_argument('-p', dest="port",
    help="Specify a port for your Spike Prime")

args = parser.parse_args()

# Parse Arguements from file
if (not (args.did and args.wid and args.eid)):
    try:
        with open("document-preferences", "r") as f: 
            args.base = f.readline().rstrip()
            args.did  = f.readline().rstrip()
            args.wid  = f.readline().rstrip()
            args.eid  = f.readline().rstrip()
    except:
        print("All parameters not given.")
        print("Please give did, wid, and eid using the flags -d, -w, and -e")
        exit()

if (not args.base):
    args.base = "https://rogers.onshape.com"
    print(". . . Defaulting to rogers.onshape.com . . .")

# Gets api key and secret key
with open("api-key", "r") as f: 
    key = f.readline().rstrip()
    secret = f.readline().rstrip()

# Setting up the client
client = Client(configuration={"base_url": args.base,
                               "access_key": key,
                               "secret_key": secret})
headers = {'Accept': 'application/vnd.onshape.v1+json; charset=UTF-8;qs=0.1',
           'Content-Type': 'application/json'}


# checkArgs() - Validates the did, wid, and eid
# Parameters:
#   verbose - boolean for excessive print statements
# Returns:
#   Nothing (wip)
def checkArgs(verbose):
    if(verbose):
        print("Using Workbench:", args.base)
        print("Document ID:", args.did)
        print("Workspace ID:", args.wid)
        print("Element ID:", args.eid)
        print()
    
    ## TODO:
    # hit api and check if did, wid, and eid are valid
    # right now checkArgs only prints args

#############################################
#                                           #
#              Making API calls             #
#                                           #
#############################################

# callAPI() - Calls the Onshape API
# Parameters:
#   endpoint - a key from the urls table
#   params   - an empty dictionary (wip)
#   payload  - request body, in json format
# Returns:
#   The response data object from the api call
def callAPI(endpoint, params, payload, hasReturn):

    method    = urls[endpoint][0]
    fixed_url = urls[endpoint][1]
    fixed_url = fixed_url.replace('did', args.did)
    fixed_url = fixed_url.replace('wid', args.wid)
    fixed_url = fixed_url.replace('eid', args.eid)
    # if (endpoint == 'assembly-definition'):
    #   fixed_url = fixed_url.replace('OPT1', "true") # Mate Features
    #   fixed_url = fixed_url.replace('OPT2', "true") # Non Solids
    #   fixed_url = fixed_url.replace('OPT3', "true") # Mate Connectors

    response = client.api_client.request(method, url=args.base + fixed_url,
        query_params=params, headers=headers, body=payload)

    # print(response.data)
    if (hasReturn):
    	return json.loads(response.data);
