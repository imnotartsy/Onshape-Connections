###############################################################################  
# Project name: Onshape Features
# File name: transforms.py
# Author: Therese (Teo) Patrosio @imnotartsy
# Date: 7/16/20
# Description: Main driver file for Onshape Features
# History: 
#    Last modified by Teo 7/2/20
# (C) Tufts Center for Engineering Education and Outreach (CEEO)
###############################################################################

from onshape_client.client import Client
import json

import utils.onshape_utils as onshape
import utils.api_utils as api
import utils.transform_utils as transform

#############################################
#                                           #
#           API Enviroment Set Up           #
#                                           #
#############################################

api.checkArgs(True)
### Most server stuff is abstracted away in api_utils

#############################################
#                                           #
#              New Feature List             #
#                                           #
#############################################

### Get Assembly Information from the API
featureListInfo = onshape.getFeatureList(True)

## Print Parts and Positions (decode their transfomation arrays)



#############################################
#                                           #
#       Prepare and Perform Transform       #
#                                           #
#############################################

### Get User Input
if (transform.promptUser("Do you want to add a feature")):

    print("Adding a feature!")

    feature = {
    "type" : 134,
    "typeName" : "BTMFeature",
    "message" : {
      "featureType" : "extrude",
      "featureId" : "FUvEB04dwEtY7pw_0",
      "name" : "Extrude 1",
      "parameters" : [ {
        "type" : 145,
        "typeName" : "BTMParameterEnum",
        "message" : {
          "enumName" : "OperationDomain",
          "value" : "MODEL",
          "namespace" : "",
          "parameterId" : "domain",
          "hasUserCode" : False,
          "nodeId" : "PvhNTaCoz1BNkX0Z"
        }
      }, {
        "type" : 145,
        "typeName" : "BTMParameterEnum",
        "message" : {
          "enumName" : "ToolBodyType",
          "value" : "SOLID",
          "namespace" : "",
          "parameterId" : "bodyType",
          "hasUserCode" : False,
          "nodeId" : "fMtQOr/uuLllZj61"
        }
      }, {
        "type" : 144,
        "typeName" : "BTMParameterBoolean",
        "message" : {
          "value" : True,
          "parameterId" : "defaultSurfaceScope",
          "hasUserCode" : False,
          "nodeId" : "4h1FtA6tvE2sCtze"
        }
      }, {
        "type" : 148,
        "typeName" : "BTMParameterQueryList",
        "message" : {
          "queries" : [ ],
          "parameterId" : "booleanSurfaceScope",
          "hasUserCode" : False,
          "nodeId" : "ldandfn7T2jVabvI"
        }
      } ],
      "suppressed" : False,
      "namespace" : "",
      "subFeatures" : [ ],
      "returnAfterSubfeatures" : False,
      "suppressionState" : {
        "type" : 0
      },
      "hasUserCode" : False,
      "nodeId" : "M8yP6w/gc5EqfeHhI"
    }
  },featureListInfo["features"][1]

    onshape.postFeature(featureListInfo["serializationVersion"],
                featureListInfo["sourceMicroversion"],
                feature, True)

else:
    print("Adding a feature will not occur.")

print()

#############################################
#                                           #
#              New Feature List             #
#                                           #
#############################################

