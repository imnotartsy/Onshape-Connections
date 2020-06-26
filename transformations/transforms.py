## Original Script written by Daniel Ryaboshapka @drybell
## Modifed by Teo Patrosio @imnotartsy

from onshape_client.client import Client
import argparse 
import json

import api_utils as util
import transform_utils as transform

# Occurance Transform: /api/assemblies/d/did/w/wid/e/eid/occurrencetransforms

#############################################
#                                           #
#             Parsing Arguements            #
#                                           #
#############################################

# Parse Arguements from the cmdline
parser = argparse.ArgumentParser(description='Onshape API')

parser.add_argument('-d', dest="did", help="Specify a document id (did) for your Onshape workspace")
parser.add_argument('-w', dest="wid", help="Specify a workspace id (wid) for your Onshape workspace")
parser.add_argument('-e', dest="eid", help="Specify an element id (eid) for your Onshape workspace")
parser.add_argument('-b', dest="base", help="Specify a base url your Onshape workspace")

args = parser.parse_args()

# Parse Arguements from file
if (not (args.did and args.wid and args.eid)):
	try:
		with open("document-preferences", "r") as f: 
			args.base = f.readline().rstrip()
			args.did = f.readline().rstrip()
			args.wid = f.readline().rstrip()
			args.eid = f.readline().rstrip()
	except:
		print("All parameters not given. Please give did, wid, and eid using the flags -d, -w, and -e")
		exit()

if (not args.base):
	args.base = "https://rogers.onshape.com"
	print(". . . Defaulting to rogers.onshape.com . . .")

print("Using Workbench:", args.base)
print("Document ID:", args.did)
print("Workspace ID:", args.wid)
print("Element ID:", args.eid)

util.openApi()


#############################################
#                                           #
#             Prepare Transform             #
#                                           #
#############################################

# prompt for type of transform
x = transform.getTransfromMatrix(1, 1, 1)

print("Transform matrix:")
transform.prettyPrintMatrix(x)
# // 'occurance-transforms': ['POST','/api/assemblies/d/did/w/wid/e/eid/occurrencetransforms']

#############################################
#                                           #
#              Process Response             #
#                                           #
#############################################

y = transform.decodeMatrix(x, True)


