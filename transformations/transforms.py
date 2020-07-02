###################################################  
# Project name: Onshape Transformations
# File name: transforms.py
# Author: Therese (Teo) Patrosio @imnotartsy
# Date: 6/26/20
# Description: Main driver file for Onshape Transformations
# Credits/inspirations: API calls referenced from Daniel Ryaboshapka @drybell
# History: 
#    Last modified by Teo 7/2/20
# (C) Tufts Center for Engineering Education and Outreach (CEEO)
###################################################

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
    print("Do you want to input a transform? ('new') or select one of the prexisting transforms:")
    print("\t", end = '')
    for transformArgName in transform.commonTransforms:
        print(transformArgName, end=", ")
    print()
    userIn = input()

    transformArgs = []
    if (userIn.upper() == 'N' or userIn.upper() == 'NEW'):
        args = transform.readInTransformObject()
    # elif (userIn == 't'): # quick transform for debugging
    #     print("\tDebugging transform selected.")
    #     args = [0.1,  0.1,  0.0,  0.0,  0.0,   0.0,   0.0]
    else:
        try:
            args = transform.commonTransforms[userIn]
        except:
            print("No transformation exists with that name. (Ending . . .)")
            exit()
    
    ## TODO: add isRelative to Transform arg object
    isRelative = transform.promptUser("Do you want the transform to be relative?")

    ### Gets Transform Matrix from Transform args object
    print("Generated transform matrix:")
    M = transform.getTranslationMatrix(args, True)
    print()

    ### Gets List of Parts to Transform
    partsToTransform = []
    print("What Parts do you want to transform?")
    for part in parts:
        query = "\tTransform {partName}?".format(partName = parts[part])
        if (transform.promptUser(query)):
            partsToTransform.append(part)
    print()

    ### Performs API call
    if (transform.promptUser("Do you want to call the api?")):
        state = onshape.postTransform(M, isRelative, partsToTransform, False)
        print("Status:", state)

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
