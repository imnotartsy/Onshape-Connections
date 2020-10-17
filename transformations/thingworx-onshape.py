###############################################################################  
# Project name: Onshape Transformations
# File name: thingworx-onshape.py
# Author: Therese (Teo) Patrosio @imnotartsy
# Date: 10/13/20
# Description: Connects spike bluetooth to onshape api for 7/7 demo
# History: 
#    Last modified by Teo 10/16/20
###############################################################################

import utils.transform_utils as transform
import utils.onshape_utils as onshape
import utils.thingworx_utils as thingworx

currentState = [0, 0, 0]

### Read Data and call API
for i in range(0,100):
   
    ## Call to thingworks
    data = thingworx.thingworxGET(["X", "Y", "Z"])

    ## Convert from thingworx inches to onshape meters
    x = float(data["X"]) * .0254
    y = float(data["Y"]) * .0254
    z = float(data["Z"]) * .0254
    currentState = [x, y, z]

    ## Get asssembly information
    assembly = onshape.getAssemblyInfo(False)

    ## Selects first element
    partsToTransform = [list(assembly.keys())[0]]

    ## Get current position, and decode
    M = assembly[partsToTransform[0]]["position"]
    position = transform.decodeMatrix(M, False)

    print("Curr pos: ", position)

    ## Checks if position is different from posted value
    ## Note: the rounding is due to floating point error
    if round(position[0], 6) != x or round(position[1], 6) != y or round(position[2], 6) != z:

        ## Sets current state to an args "struct"
        args = currentState + [0, 0, 0, 0]
        
        ## Transforms set up (get matrix and part id from assembly info)
        M = transform.getTranslationMatrix(args, False)

        ## Call API
        state = onshape.postTransform(M, False, [partsToTransform], False)
        print("\tTransformation status:", state)

