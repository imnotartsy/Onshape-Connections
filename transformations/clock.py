###############################################################################  
# Project name: Onshape Clock
# File name: clock.py
# Author: Therese (Teo) Patrosio @imnotartsy
# Date: 10/26/20
# Description: ONSHAPE CLOCK
# History: 
#    Last modified by Teo 10/26
###############################################################################

# from onshape_client.client import Client
import json

import utils.onshape_utils as onshape
import utils.api_utils as api
import utils.transform_utils as transform
import datetime

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

while True:
    now=datetime.datetime.now()
    print("Current Time:", ('%02d:%02d.%02d'%(now.hour,now.minute,now.second)))

    if configInfo["configurationParameters"][3]["message"]["rangeAndDefault"]["message"]["defaultValue"] != (now.second * 6):
        
        newConfigs = {}
        newConfigs["Rotation"] = (now.minute * 6);
        newConfigs["HourRotation"] = (now.hour * 30);
        newConfigs["SecondRotation"] = (now.second * 6);

        state = onshape.setConfigurations(newConfigs, configInfo, False)
        print("\tUpdate Status:", state)





