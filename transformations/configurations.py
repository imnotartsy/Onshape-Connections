###############################################################################  
# Project name: Onshape Configurations
# File name: configurations.py
# Author: Therese (Teo) Patrosio @imnotartsy
# Date: 10/24/20
# Description: Main driver file for Onshape Configurations
# History: 
#    Last modified by Teo 10/24
###############################################################################

# from onshape_client.client import Client
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
#            Configurations Info            #
#                                           #
#############################################

### Get Configuration Information from the API
configInfo = onshape.getConfigurations(False)

print()

# print(configInfo["configurationParameters"][0]["message"]["parameterId"])

for config in configInfo["configurationParameters"]:
    print(config["message"]["parameterId"])
    try:
        print("\tDefault value: ",
            config["message"]["rangeAndDefault"]["message"]["defaultValue"])
        print("\tMax value: ",
            config["message"]["rangeAndDefault"]["message"]["maxValue"])
        print("\tMin value: ",
            config["message"]["rangeAndDefault"]["message"]["minValue"])
    except:
        print("There are no values for this configuration.")

    print()


#############################################
#                                           #
# Prepare and Perform Configurations Update #
#                                           #
#############################################

# ### Get User Input
if (transform.promptUser("Do you want to edit configurations?")):
    print()

    newConfigs = {}
    print("What Parts do you want to transform?")
    for config in configInfo["configurationParameters"]:
        query = "\tEdit {field}?".format(field = config["message"]["parameterId"])
        if (transform.promptUser(query)):
            
            try:
                print("Old default value: ", config["message"]["rangeAndDefault"]["message"]["defaultValue"])
                print("\tEnter new value:")
                newVal = input()

                newConfigs[config["message"]["parameterId"]] = newVal;
            except:
                print("This value is not setable.")

        
    # print(newConfigs)

    ### Performs API call
    if (transform.promptUser("Do you want to call the api?")):
        state = onshape.setConfigurations(newConfigs, configInfo, False)
        print("Status:", state)

else:
    print("A transform will not occur.")

print()


#############################################
#                                           #
#          New Configurations Info          #
#                                           #
#############################################

### Get Configuration Information from the API
configInfo = onshape.getConfigurations(False)

print()

for config in configInfo["configurationParameters"]:
    print(config["message"]["parameterId"])
    try:
        print("\tDefault value: ",
            config["message"]["rangeAndDefault"]["message"]["defaultValue"])
        print("\tMax value: ",
            config["message"]["rangeAndDefault"]["message"]["maxValue"])
        print("\tMin value: ",
            config["message"]["rangeAndDefault"]["message"]["minValue"])
    except:
        print("There are no values for this configuration.")

    print()
