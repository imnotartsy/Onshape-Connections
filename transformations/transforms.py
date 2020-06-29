## Original Script written by Daniel Ryaboshapka @drybell
## Modifed by Teo Patrosio @imnotartsy

from onshape_client.client import Client
import json

import onshape_utils as onshape
import api_utils as api
import transform_utils as transform

#############################################
#                                           #
#             Set Up Information            #
#                                           #
#############################################

api.checkArgs(True)
### Most server stuff is abstracted away in api_utils

#############################################
#                                           #
#               Assembly Info               #
#                                           #
#############################################

assembly = onshape.getAssemblyInfo(True)
parts = assembly[0]
positions = assembly[1]

### Print combined
for identifier in positions:
    print(parts[identifier], "(" + identifier + ")")
    transform.prettyPrintMatrix(positions[identifier])
    print()




## TODO: refactor page so the assembly information is in two separate functions


#############################################
#                                           #
#             Prepare Transform             #
#                                           #
#############################################

# prompt for type of transform
# x = transform.getTransfromMatrix(1, 1, 1)

# print("Transform matrix:")
# transform.prettyPrintMatrix(x)
# // 'occurance-transforms': ['POST','/api/assemblies/d/did/w/wid/e/eid/occurrencetransforms']
M = transform.getTransfromMatrix(0.5, 0.5, 0.5)
print("Generated transform matrix:")
transform.prettyPrintMatrix(M)

## TODO: prompt user for which part names
#  - then convert to part keys (id/paths)
partsToTransform = [list(parts.keys())[0]]
# print(partsToTransform)

# WIP
#  state = onshape.postTransform(M, True, partsToTransform, assembly, True)
#  print(state)

#############################################
#                                           #
#              Process Response             #
#                                           #
#############################################

# y = transform.decodeMatrix(x, True)


