## Teo Patrosio @imnotartsy

from onshape_client.client import Client
import json

import onshape_utils as onshape
import api_utils as api
import transform_utils as transform

#############################################
#                                           #
#           API Enviroment Set Up           #
#                                           #
#############################################

api.checkArgs(True)
### Most server stuff is abstracted away in api_utils

#############################################
#                                           #
#               Assembly Info               #
#                                           #
#############################################

### Get Assembly Information from the API
assembly = onshape.getAssemblyInfo(True)
parts = assembly[0]
positions = assembly[1]

### Print Parts and Positions (decode their transfomation arrays)
for identifier in positions:
    print(parts[identifier], "(" + identifier + ")")
    # transform.prettyPrintMatrix(positions[identifier])
    transform.decodeMatrix(positions[identifier], True)
    print()

#############################################
#                                           #
#       Prepare and Perform Transform       #
#                                           #
#############################################

### Get User Input
if (transform.promptUser("Do you want to perform a transform?")):

    ### Get User Transform args object
    # args = transform.readInTransformObject()
    args = [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 30]

    ## TODO: add isRelative to Transform arg object

    ### Gets Transform Matrix from Transform args object
    print("Generated transform matrix:")
    M = transform.getTranslationMatrix(args, True)
    print()

    ### Gets List of Parts to Transform
    partsToTransform = []
    for part in parts:
        if (parts[part] == "axle <1>"):
            partsToTransform.append(part)
            print("Transforming", parts[part], "(" + part + ")")
    print()

    ### Performs API call
    if (transform.promptUser("Do you want to call the api?")):
        if (transform.promptUser("Do you want to call it once?")):
            state = onshape.postTransform(M, True, partsToTransform, False)
            print("Status:", state)
        if (transform.promptUser("Do you want to call it ten times?")):
            for i in range(0, 11):
                print("Round", i)
                state = onshape.postTransform(M, True, partsToTransform, False)
                print("Status:", state)

                assembly2 = onshape.getAssemblyInfo(False)
                positions2 = assembly2[1]

                transform.decodeMatrix(positions2[partsToTransform[0]], True)
                print()


else:
    print("A transform will not occur.")

print()

#############################################
#                                           #
#             New Assembly Info             #
#                                           #
#############################################

### Get Assembly Information from the API
assemblyAfter = onshape.getAssemblyInfo(False)
partsAfter = assemblyAfter[0]
positionsAfter = assemblyAfter[1]

### Print Parts and Positions
for identifier in positions:
    print(partsAfter[identifier], "(" + identifier + ")")
    transform.decodeMatrix(positionsAfter[identifier], True)
    print()
