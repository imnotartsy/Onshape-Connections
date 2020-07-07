###############################################################################
# Project name: Onshape Transformations
# File name: transform_utils.py
# Author: Therese (Teo) Patrosio @imnotartsy
# Date: 6/26/20
# Description: Functions to do with transform arg objects and transform matrces
# Credits/inspirations: Transform matrix math help from Andrew Daetz and Milan
# History: 
#    Last modified by Teo 7/2/20
# (C) Tufts Center for Engineering Education and Outreach (CEEO)
###############################################################################

import math

#############################################
#                                           #
#              Common Transforms            #
#                                           #
#############################################

# commonTransformations is a dicionary of "transform args" objects used mostly in 
#  this file. A transform args objects is an array of seven values:
#  [tx, ty, tz, rx, ry, rz, w] (translate x, y, z, then the rotation axis and angle)
commonTransforms = {
                    #[ tx,   ty,   tz,   rx,   ry,   rz,   w  ]
    'transUp' :      [ 0.0,  0.0,  1.0,  0.0,  0.0,   0.0,   0.0],
    'transDown':     [ 0.0,  0.0, -1.0,  0.0,  0.0,   0.0,   0.0],
    'transRight':    [ 1.0,  0.0,  0.0,  0.0,  0.0,   0.0,   0.0],
    'transLeft':     [-1.0,  0.0,  0.0,  0.0,  0.0,   0.0,   0.0],
    'transForward':  [ 0.0,  1.0,  0.0,  0.0,  0.0,   0.0,   0.0],
    'transBackwards':[ 0.0, -1.0,  0.0,  0.0,  0.0,   0.0,   0.0],
    'rot30ccZ':      [ 0.0,  0.0,  0.0,  0.0,  0.0,   1.0,   30.0],
    'rot90ccZ':      [ 0.0,  0.0,  0.0,  0.0,  0.0,   1.0,   90.0],


    'leftside':      [ 0.0,  0.0,  0.0,  1.0,  0.0,   0.0,  -90.0], # 5
    'rightside':     [ 0.0,  0.0,  0.0,  1.0,  0.0,   0.0,   90.0], # 2
    'down':          [ 0.0,  0.0,  0.0,  1.0,  0.0,   0.0,  180.0], # 6
    'up':            [ 0.0,  0.0,  0.0,  0.0,  0.0,   1.0,   90.0], # 1 
    'front':         [ 0.0,  0.0,  0.0,  0.0,  1.0,   0.0,   90.0], # 3
    'back':          [ 0.0,  0.0,  0.0,  0.0,  1.0,   0.0,  -90.0], # 4
}

#############################################
#                                           #
#            User Input functions           #
#                                           #
#############################################

# readInTransformObject() - Creates transform args objects (as defined above)
# Parameters:
#   None
# Returns:
#   A transform args object
def readInTransformObject():
    args = []
    dim  = ["tx", "ty", "tz", "rx", "ry", "rz", "alpha (degree)"]
    for i in range(0,7):
        print("Please Enter {name} value:".format(name = dim[i]))
        try:
            args.append(float(input()))
        except:
            print("The input entered is not valid. (Ending . . .)")
            exit()
    
    return args

# promtUser() - Asks user a query string that has a yes or no answer
# Parameters:
#   queryString - The question for the user
# Returns:
#   A boolean value depending on the user's input
def promptUser(questionString):
    print(questionString, "(y/n)")
    userIn = input()
    if (userIn.upper() == 'Y' or userIn.upper() == 'YES'):
        return True
    elif (userIn.upper() == 'N' or userIn.upper() == 'NO'):
        return False
    else:
        print("The input entered is not valid.")
        return False


#############################################
#                                           #
#             Matrix Operations             #
#                                           #
#############################################

# A transform matrix as defined here:
#    https://drafts.csswg.org/css-transforms-2/#mathematical-description
# In this program a transform matrix will be a 16 element 1D array that
#   should be visualized as a 4x4 2D matrix.

# Matrix format
#   M[0]  = m11     M[1]  = m21     M[2]  = m31     M[3]  = m41
#   M[4]  = m12     M[5]  = m22     M[6]  = m32     M[7]  = m42
#   M[8]  = m13     M[9]  = m23     M[10] = m33     M[11] = m43
#   M[12] = m14     M[13] = m24     M[14] = m34     M[15] = m44


# getTranslationMatrix() - Generates a transform matrix from a transform
#   args object
# Parameters:
#   translation - a tranform args object (array)
#   verbose - a boolean value for if the matrix should be printed
# Returns:
#   A transform matrix.
def getTranslationMatrix(translation, verbose):

    # Translate variables
    tx = translation[0]
    ty = translation[1]
    tz = translation[2]
    # Vector for Rotation
    rx = translation[3]
    ry = translation[4]
    rz = translation[5]
    # Angle for Rotation
    w_deg = translation[6]
    if (w_deg == 0):
        return [1.0,  0.0,  0.0,  tx,
                0.0,  1.0,  0.0,  ty,
                0.0,  0.0,  1.0,  tz,
                0.0,  0.0,  0.0,  1.0]

    # Unit Vector for Rotation
    rotLen = math.sqrt(math.pow(rx, 2) + math.pow(ry, 2) + math.pow(rz, 2))
    ux = rx / rotLen
    uy = ry / rotLen
    uz = rz / rotLen

    w = math.radians(w_deg)

    sc = math.sin(w/2) * math.cos(w/2)
    sq = math.pow(math.sin(w/2), 2)

    M = [1.0 - 2.0 * (math.pow(uy, 2) + math.pow(uz, 2)) * sq,  # m11
         2.0 * (ux * uy * sq - uz * sc),                        # m21
         2.0 * (ux * uz * sq + uy * sc),                        # m31
         tx,                                                    # m41
         2.0 * (ux * uy * sq + uz * sc),                        # m12
         1.0 - 2.0 * (math.pow(ux, 2) + math.pow(uz, 2)) * sq,  # m22
         2.0 * (uy * uz * sq - ux * sc),                        # m32
         ty,                                                    # m42
         2.0 * (ux * uz * sq - uy * sc),                        # m13
         2.0 * (uy * uz * sq + ux * sc),                        # m23
         1.0 - 2.0 * (math.pow(ux, 2) + math.pow(uy, 2)) * sq,  # m33
         tz,                                                    # m43
         0.0,                                                   # m43
         0.0,                                                   # m43
         0.0,                                                   # m43
         1.0]                                                   # m43

    if (verbose):
        prettyPrintMatrix(M)
    return M

# getTranslationMatrix() - Generates translation args object from a transform
#   matrix
# Parameters:
#   M - a transformation matrix
#   vebrose - a boolean value for if the generated transform args object should
#       should be printed
# Returns:
#   a tranform args object (array)
#
def decodeMatrix(M, verbose):

    tx = M[3]
    ty = M[7]
    tz = M[11]

    w_rad = 1/2 * math.acos(1 - 1/2 * (math.pow((M[9] - M[6]),2) + math.pow((M[2] - M[8]),2) + pow((M[4] - M[1]),2)))
    sc = math.sin(w_rad/2) * math.cos(w_rad/2)

    if (sc != 0):
        x = (M[9] - M[6])/(4 * sc)
        y = (M[2] - M[8])/(4 * sc)
        z = (M[4] - M[1])/(4 * sc)
    else:
        x = 0
        y = 0
        z = 0

    w = math.degrees(w_rad)

    translation = [tx, ty, tz, x, y, z, w]

    if (verbose):
        prettyPrintPosition(translation)
    return translation

#############################################
#                                           #
#          General Helper Functions         #
#                                           #
#############################################

## TODO: convert to .format() for accurate tab spacing

def prettyPrintMatrix(x):
    col = math.sqrt(len(x))
    for i in range(0, len(x)):
        if (i%col == 0 and i != 0):
            print()
        print(x[i], end='\t')
    print()


def prettyPrintPosition(posArray):
    print("Translation (x, y, z): \t\t", round(posArray[0], 5),
                                   '\t', round(posArray[1], 5),
                                   '\t', round(posArray[2], 5))
    print("Rotation (ux, uy, uz, alpha): \t", round(posArray[3], 5),
                                        '\t', round(posArray[4], 5),
                                        '\t', round(posArray[5], 5),
                                        '\t', round(posArray[6], 5))
    # print("Rotation unrounded: \t", posArray[3],
    #                           '\t', posArray[4],
    #                           '\t', posArray[5],
    #                           '\t', posArray[6])
