###############################################################################  
# Project name: Onshape Transformations
# File name: onshape_utils.py
# Author: Therese (Teo) Patrosio @imnotartsy
# Date: 6/26/20
# Description: Functions for specific onshape API calls; uses api_utils.py
# History: 
#    Last modified by Teo 7/25/20
# (C) Tufts Center for Engineering Education and Outreach (CEEO)
###############################################################################
import utils.api_utils as api
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

    response = api.callAPI('assembly-definition', payload , params, True)
    # print(response)

    ### Return Data Structure: a dict of part-objects with their id as the key
    #     assemblyReturn = {
    #         part_id : {
    #             "fullId": [],
    #             "position": [], # transformation matrix
    #             "partName": ""
    #             "type": ""
    #         }
    #     }

    assemblyReturn = {}

    ### Gets Positions and Paths
    for occurrence in response["rootAssembly"]["occurrences"]:
        # Creates each part-object
        part = {
            "fullPath": occurrence["path"],
            "position": occurrence["transform"],
            "partName": "",
            "type": ""
        }
        assemblyReturn[occurrence["path"][len(occurrence["path"])-1]] = part
        

    ### Gets Part Names and Part Types
    if (verbose):
        print("Parts in assembly:")

    for instance in response["rootAssembly"]["instances"]:
        if(verbose): print("  ", instance["id"], ":", instance["name"])
        assemblyReturn[instance["id"]]["partName"] = instance["name"]
        assemblyReturn[instance["id"]]["type"] = instance["type"]
    
    # Now Prints individual parts in subassemblies!
    for assembly in response["subAssemblies"]:
        for instance in assembly["instances"]:
            if(verbose): print("  ", instance["id"], ":", instance["name"])
            assemblyReturn[instance["id"]]["partName"] = instance["name"]
            assemblyReturn[instance["id"]]["type"] = instance["type"]
    if(verbose): print()

    
    # Debug Printing
    # for partID in assemblyReturn:
    #     print(partID)
    #     # print("\t", assemblyReturn[partID])
    #     print("\t", assemblyReturn[partID]["fullId"])
    #     print("\t", assemblyReturn[partID]["position"])
    #     print("\t", assemblyReturn[partID]["partName"])
    #     print("\t", assemblyReturn[partID]["type"])

    return assemblyReturn

#############################################
#                                           #
#       Occurence Transforms API Call       #
#                                           #
#############################################


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
            "path": part
        }
        payload["occurrences"].append(occurance)
    # print(json.dumps(payload, indent = 2)) # debugging for printing payload

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


#############################################
#                                           #
#              Feature API Calls            #
#                                           #
#############################################

# getFeatureList() - for getting feature list (7.16.20)
#   for onshape- team
# Parameters:
#
# Returns:
#
# def getFeatureList(verbose):
#     payload = {}
#     params = {}

#     response = api.callAPI('feature-list', payload , params, True)

#     featureReturn = {}

#     featureReturn["serializationVersion"]   = response["serializationVersion"]
#     featureReturn["sourceMicroversion"]     = response["sourceMicroversion"]

#     featureReturn["features"] = response["features"]

#     if(verbose):
#         print(json.dumps(response, indent = 2)) # debugging for printing payload

#     return featureReturn

# postFeature() - for editting features (7.16.20)
#   for onshape- team
# Parameters:
#
# Returns:
#
# def postFeature(serialV, microV, feature, verbose):
#     payload = {
#       "feature": feature,
#       "serializationVersion": serialV,
#       "sourceMicroversion": microV
#     }
#     params = {}

#     try:
#         response = api.callAPI('add-feature', payload , params, True)
#     except ApiException as error:
#         print("Invalid Request!")
#         print("Sever message:", error.body)
#         print("Ending. . .")
#         exit();

#     print(json.dumps(response, indent = 2)) # debugging for printing payload

#     return response


