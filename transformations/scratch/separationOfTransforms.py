###############################################################################
# Project name: Separation of transforms
# File name: transform_utils.py
# Author: Therese (Teo) Patrosio @imnotartsy
# Date: 6/26/20
# Description: Functions to do with transform arg objects and transform matrces
# Credits/inspirations: Transform matrix math help from Andrew Daetz and Milan
# History: 
#    Last modified by Teo 8/4/20
# (C) Tufts Center for Engineering Education and Outreach (CEEO)
###############################################################################

import utils.transform_utils as transform

OG = [-3.4041840642415265e-17,    -5.089747088344418e-17,        1.0000000000000013,      -0.01123750000000001,    
          -0.7071067811865491,        0.7071067811865483,    1.1918730444604661e-17,     1.117412882486946e-18,    
           -0.707106781186549,       -0.7071067811865483,    -6.006116316925195e-17,    -8.900969324187317e-18,
                            0,                         0,                         0,                         1]  

print("Curr Pos")
transform.prettyPrintMatrix(OG)
transform.decodeMatrix(OG, True)

print()

print("Removal Matrix")
remove = transform.getTranslationMatrix(transform.commonTransforms['rot90ccY'], True)
transform.prettyPrintPosition(transform.commonTransforms['rot90ccY'])

print()

print("Function")
hope = transform.removeRot(OG, remove, True)
transform.decodeMatrix(hope, True)