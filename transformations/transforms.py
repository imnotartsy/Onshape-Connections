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
    # transform.prettyPrintMatrix(positions[identifier])
    transform.decodeMatrix(positions[identifier], True)
    print()

#############################################
#                                           #
#             Prepare Transform             #
#                                           #
#############################################

### Get User Input
print("Do you want to perform a transform? (y/n)")
userIn = input()

if (userIn.upper() == 'Y' or userIn.upper() == 'YES'):


    print("Do you want to input a transform? ('new') or select one of the prexisting transforms:")
    print("\t", end = '')
    for transformArgName in transform.commonTransforms:
        print(transformArgName, end=", ")
    print()
    userIn = input()

    transformArgs = []
    if (userIn.upper() == 'N' or userIn.upper() == 'NEW'):
        args = transform.readInTransformObject()
    else:
        try:
            args = transform.commonTransforms[userIn]
        except:
            print("No transformation exists with that name")

    # Gets transform matrix
    M = transform.getTranslationMatrix(args)
    print("Generated transform matrix:")
    transform.prettyPrintMatrix(M)

    ## TODO: prompt user for which part names
    #  - then convert to part keys (id/paths)
    partsToTransform = [list(parts.keys())[1]] # grabs box
    # print(partsToTransform)


    print("Do you want to call the api? (y/n)")
    userIn = input()

    if (userIn.upper() == 'Y' or userIn.upper() == 'YES'):
        state = onshape.postTransform(M, True, partsToTransform, assembly, False)
        print("Status:", state)

print()

#############################################
#                                           #
#              Process Response             #
#                                           #
#############################################

assemblyAfter = onshape.getAssemblyInfo(False)
partsAfter = assemblyAfter[0]
positionsAfter = assemblyAfter[1]

### Print combined
for identifier in positions:
    print(partsAfter[identifier], "(" + identifier + ")")
    # transform.prettyPrintMatrix(positions[identifier])
    transform.decodeMatrix(positionsAfter[identifier], True)
    print()


