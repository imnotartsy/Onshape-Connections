## Original Script written by Daniel Ryaboshapka @drybell
## Modifed by Teo Patrosio @imnotartsy

from onshape_client.client import Client
import json

import api_utils as util
import transform_utils as transform

#############################################
#                                           #
#             Set Up Information            #
#                                           #
#############################################

util.checkArgs(True)
### Most server stuff is abstracted away in api_utils

#############################################
#                                           #
#               Assembly Info               #
#                                           #
#############################################

### Gets Assembly Information
payload = {}
params = {}

response = util.callAPI('assembly-definition', {} , {})
# print(json.dumps(response, indent = 2))


### Creates Part List
parts = {}

print("Parts in assembly:")
for instance in response["rootAssembly"]["instances"]:
	print("  ", instance["id"], ":", instance["name"])
	parts[instance["id"]] = instance["name"]
print()


### Gets current position
positions = {}

# print("Positions of parts")
for occurrence in response["rootAssembly"]["occurrences"]:
	# print("  ", occurrence["path"][0],":", occurrence["transform"])
	positions[occurrence["path"][0]] = occurrence["transform"]
print()


### Print combined
for identifier in positions:
	print(parts[identifier], "(" + identifier + ")", end = "")
	transform.prettyPrintMatrix(positions[identifier])
	print()




## TODO: refactor page so the assembly information is in two separate functions


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


