###############################################################################  
# Project name: Chess
# File name: chess.py
# Author: Therese (Teo) Patrosio @imnotartsy
# Date: 10/29/20
# Description: Connects Thingworx thing to Onshape, performs transforms based
#   based on thing values
# History: 
#    Last modified by Teo 10/29/20
###############################################################################

import utils.transform_utils as transform
import utils.onshape_utils as onshape
import utils.thingworx_utils as thingworx


### Read Data and call API
for i in range(0,1000):
   
    ## Call to thingworks
    data = thingworx.thingworxGET(["White_Pawn_X", "White_Pawn_Y", "Black_Pawn_X", "Black_Pawn_Y"])
    print(data)

    ## Convert from thingworx units to chessboard squares
    wpx = float(data["White_Pawn_X"]) * .1 + .05
    wpy = float(data["White_Pawn_Y"]) * -.1 - .05
    bpx = float(data["Black_Pawn_X"]) * .1  - .06
    bpy = float(data["Black_Pawn_Y"]) * -.1 - .05

    wpcurrentState = [wpx, wpy, .0101]
    bpcurrentState = [bpx, bpy, .0101]

    ## Get asssembly information
    assembly = onshape.getAssemblyInfo(False)



    ### white pawn

    ## Get current position, and decode
    M = assembly["MZYDVMyh+P+j3aAkE"]["position"]
    position = transform.decodeMatrix(M, False)

    print("Curr pos bp: ", position)

    ## Checks if position is different from posted value
    ## Note: the rounding is due to floating point error
    if round(position[0], 6) != wpx or round(position[1], 6) != wpy:

        ## Sets current state to an args "struct"
        args = wpcurrentState + [0, 0, 0, 0]
        print(args)
        
        ## Transforms set up (get matrix and part id from assembly info)
        M = transform.getTranslationMatrix(args, False)

        ## Call API
        state = onshape.postTransform(M, False, [["MZYDVMyh+P+j3aAkE"]], False)
        print("\tTransformation status:", state)



    ### black pawn

    ## Get current position, and decode
    M = assembly["MGaR3QdoOeRihuupb"]["position"]
    position = transform.decodeMatrix(M, False)

    print("Curr pos wp: ", position)

    ## Checks if position is different from posted value
    ## Note: the rounding is due to floating point error
    if round(position[0], 6) != bpx or round(position[1], 6) != bpy:

        ## Sets current state to an args "struct"
        args = bpcurrentState + [0, 0, 0, 0]
        
        ## Transforms set up (get matrix and part id from assembly info)
        M = transform.getTranslationMatrix(args, False)

        ## Call API
        state = onshape.postTransform(M, False, [["MGaR3QdoOeRihuupb"]], False)
        print("\tTransformation status:", state)