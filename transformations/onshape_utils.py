###############################################################################
# Project name: Onshape Transformations
# File name: onshape_utils.py
# Author: Therese (Teo) Patrosio @imnotartsy
# Date: 6/28/20
# Description: Functions to do with calling the onshape API, specifically
#    the assembly and transform endpoints
# Credits/inspirations: Transform matrix math help from Andrew Daetz and Milan
# History: 
#    Last modified by Teo 7/2/20
# (C) Tufts Center for Engineering Education and Outreach (CEEO)
###############################################################################

import api_utils as api
import json

from onshape_client.oas.exceptions import ApiException

#############################################
#                                           #
#             Assembly API Call             #
#                                           #
#############################################

# getAssemblyInfo() - Calls 'assembly-definition' and returns a part and
#      position list
# Parameters:
#   verbose - boolean for excessive print statements
# Returns:
#   - An assembly object (a list):
#      - The first element is a part dictionary where the keys are part id's
#    and the values are the names of the parts
#      - The second element is a posision dictionary where the keys are part
#   id's and the values are transformation matrices
def getAssemblyInfo(verbose):
    payload = {}
    params = {}

    response = api.callAPI('assembly-definition', payload, params, True)
    # print(response)

    ### Creates Part List
    parts = {}

    if (verbose):
        print("Parts in assembly:")
    for instance in response["rootAssembly"]["instances"]:
        if(verbose): print("  ", instance["id"], ":", instance["name"])
        parts[instance["id"]] = instance["name"]
    if(verbose): print()


    ### Gets current position
    positions = {}

    # print("Positions of parts")
    for occurrence in response["rootAssembly"]["occurrences"]:
        # print("  ", occurrence["path"][0],":", occurrence["transform"])
        positions[occurrence["path"][0]] = occurrence["transform"]

    return [parts, positions]


# postTransform() - Calls 'occurence-transforms'
# Parameters:
#   M - a transform matrix
#   parts - an array of part names to apply the transformation to
#   relative - boolean for if the transform is relative (wip)  
#   assembly - (as defined above in getAssemblyInfo) 
#   verbose - boolean for excessive print statements
# Returns:
#   Nothing (success code/wip)
def postTransform(M, isRelative, parts, verbose):
    
    payload = {
        "occurrences": [],
        "transform": M,                          
        "isRelative": isRelative
    }

    for part in parts:
        occurance = {
            "path": [part]
        }
        payload["occurrences"].append(occurance)
    # print(json.dumps(payload, indent = 2))

    if (verbose): print(payload)
    params = {}

    try:
        response = api.callAPI('occurrence-transforms', params, payload, False)
    except ApiException as error:
        print("Invalid transform!")
        print("Sever message:", error.body)
        print("Ending. . .")
        exit();

    return "success"