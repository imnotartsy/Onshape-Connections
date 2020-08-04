###############################################################################
# Project name: Onshape Transformations
# File name: transform_utils.py
# Author: Therese (Teo) Patrosio @imnotartsy
# Date: 6/26/20
# Description: Functions to do with transform arg objects and transform matrces
# Credits/inspirations: Transform matrix math help from Andrew Daetz and Milan
# History: 
#    Last modified by Teo 8/4/20
# (C) Tufts Center for Engineering Education and Outreach (CEEO)
###############################################################################

import math
import numpy as np
import copy

### Note
# There are three main types of data structures in this file:
#  - transform args
#  - transformation matrices
#  - normal 2D matrices (only internal temps use and are never parameters)
# These are defined as they are used.


#############################################
#                                           #
#              Common Transforms            #
#                                           #
#############################################

# commonTransformations is a dicionary of "transform args" objects used mostly in 
#  this file. A transform args objects is an array of seven values:
#  [tx, ty, tz, rx, ry, rz, w] (translate x, y, z, then the rotation axis and angle)
commonTransforms = {
                    #[ tx,   ty,   tz,   rx,   ry,    rz,   w    ]
    'transUp' :      [ 0.0,  0.0,  1.0,  0.0,  0.0,   0.0,    0.0],
    'transDown':     [ 0.0,  0.0, -1.0,  0.0,  0.0,   0.0,    0.0],
    'transRight':    [ 1.0,  0.0,  0.0,  0.0,  0.0,   0.0,    0.0],
    'transLeft':     [-1.0,  0.0,  0.0,  0.0,  0.0,   0.0,    0.0],
    'transForward':  [ 0.0,  1.0,  0.0,  0.0,  0.0,   0.0,    0.0],
    'transBackwards':[ 0.0, -1.0,  0.0,  0.0,  0.0,   0.0,    0.0],
    'rot30ccZ':      [ 0.0,  0.0,  0.0,  0.0,  0.0,   1.0,   30.0],
    'rot90ccZ':      [ 0.0,  0.0,  0.0,  0.0,  0.0,   1.0,   90.0],
    # 'rot180ccZ':     [ 0.0,  0.0,  0.0,  0.0,  0.0,   1.0,  180.0],

    # Dice Demo transforms
    'leftside':      [ 0.0,  0.0,  0.0,  1.0,  0.0,   0.0,  -90.0], # 5
    'rightside':     [ 0.0,  0.0,  0.0,  1.0,  0.0,   0.0,   90.0], # 2
    'down':          [ 0.0,  0.0,  0.0,  1.0,  0.0,   0.0,  180.0], # 6
    'up':            [ 0.0,  0.0,  0.0,  0.0,  0.0,   1.0,   90.0], # 1 
    'front':         [ 0.0,  0.0,  0.0,  0.0,  1.0,   0.0,   90.0], # 3
    'back':          [ 0.0,  0.0,  0.0,  0.0,  1.0,   0.0,  -90.0], # 4

    # Color Demo transforms
    'yellow':        [ 0.0,  0.0,  0.0,  0.0,  0.0,   1.0,    -30],
    'red':           [ 0.0,  0.0,  0.0,  0.0,  0.0,   1.0,    -15],
    'blue':          [ 0.0,  0.0,  0.0,  0.0,  0.0,   1.0,      1], # offset
    'green':         [ 0.0,  0.0,  0.0,  0.0,  0.0,   1.0,   30.0],

    # Two Motor Demo transforms
    'rot90ccY':      [ 0.0,  0.0,  0.0,  0.0,  1.0,   0.0,     90]
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


# getTranslationMatrix() - Generates a transform matrix from a transform args
#   object
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

    try:
        w_rad = 1/2 * math.acos(1 - 1/2 * (math.pow((M[9] - M[6]),2) + math.pow((M[2] - M[8]),2) + pow((M[4] - M[1]),2)))
    except:
        print("Out of bounds, position may be printed wrong")
        w_rad = 1/2 * math.acos(2 - 1/2 * (math.pow((M[9] - M[6]),2) + math.pow((M[2] - M[8]),2) + pow((M[4] - M[1]),2)))
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


# returnToOriginx() - Generates a transform args from a transform args object
#   that reorients to the origin
# Parameters:
#   translation - a tranform args object (array)
#   verbose - a boolean value for if the new transform args should be printed
# Returns:
#   A transform matrix.
def returnToOriginx(translation, verbose):

    new_translation = copy.deepcopy(translation)

    # Flips translation and "unrotates"
    new_translation[0] = -new_translation[0] # tx
    new_translation[1] = -new_translation[1] # ty
    new_translation[2] = -new_translation[2] # tz

    new_translation[6] = -new_translation[6] # w

    if (verbose):
        prettyPrintPosition(new_translation)
    return translation


# removeRot() - Removes a rotation from a parent transformation
# Parameters:
#   M - a transformation matrix
#   remove - a transformat
#   verbose - a boolean value for if the new transform args should be printed
# Returns:
#   A transform matrix.
def removeRot(M, remove, verbose): #remove, 

    removeInv = inverse(remove)

    ## Uses multiply Inner so the tx, ty, tz values do not interfere
    result = multiplyInner(M, removeInv)

    if (verbose):
        prettyPrintMatrix(result)
    return result



#############################################
#                                           #
#           Matrix Math (Generic)           #
#                                           #
#############################################

# These functinos use the numpy linalg library which requires standard
# 2D matrices.

# Matrix format
#   M[0]     M[1]     M[2]     M[3]
#   M[4]     M[5]     M[6]     M[7]
#   M[8]     M[9]     M[10]    M[11]
#   M[12]    M[13]    M[14]    M[15]

# inverse() - creates the inverse matrix
# Parameters:
#   M - the input transformation matrix
# Returns:
#  The resultant transformation matrix
def inverse(M):    
    X = np.array([[M[0],   M[1],   M[2],    M[3]],
                  [M[4],   M[5],   M[6],    M[7]],
                  [M[8],   M[9],  M[10],   M[11]],
                 [M[12],  M[13],  M[14],   M[15]]])

    Z = np.linalg.inv(X)
    C = [Z[0][0],   Z[0][1],  Z[0][2],  Z[0][3],
         Z[1][0],   Z[1][1],  Z[1][2],  Z[1][3],
         Z[2][0],   Z[2][1],  Z[2][2],  Z[2][3],
         Z[3][0],   Z[3][1],  Z[3][1],  Z[3][3]]
    return C


# multiply() - Multiplies matrix A and B
# Parameters:
#   A - the first transformation matrix
#   B - the second transformation matrix
# Returns:
#   The resultant transformation matrix
def multiply(A, B):
    X = ([[A[0],   A[1],   A[2],    A[3]],
          [A[4],   A[5],   A[6],    A[7]],
          [A[8],   A[9],  A[10],   A[11]],
         [A[12],  A[13],  A[14],   A[15]]])

    Y = ([[B[0],   B[1],   B[2],    B[3]],
          [B[4],   B[5],   B[6],    B[7]],
          [B[8],   B[9],  B[10],   B[11]],
         [B[12],  B[13],  B[14],   B[15]]])

    Z = np.matmul(X, Y)

    C = [Z[0][0],   Z[0][1],  Z[0][2],  Z[0][3],
         Z[1][0],   Z[1][1],  Z[1][2],  Z[1][3],
         Z[2][0],   Z[2][1],  Z[2][2],  Z[2][3],
         Z[3][0],   Z[3][1],  Z[3][1],  Z[3][3]]

    return C


# multiplyInner() - Multiplies matrix A and B
#   Note this function assumes these will be 4x4 matrices and will multiply the
#      inside 3x3 (in the top left)
# Parameters:
#   A - the first transformation matrix
#   B - the second transformation matrix
# Returns:
#   The resultant transformation matrix (with the original matrices outer edge values)
def multiplyInner(A, B):
    X = np.array([[A[0], A[1], A[2]], [A[4], A[5], A[6]], [A[8], A[9], A[10]]])
    Y = np.array([[B[0], B[1], B[2]], [B[4], B[5], B[6]], [B[8], B[9], B[10]]])

    Z = np.matmul(X, Y)
    C = [Z[0][0],   Z[0][1],  Z[0][2],   A[3],
         Z[1][0],   Z[1][1],  Z[1][2],   A[6],
         Z[2][0],   Z[2][1],  Z[2][2],  A[11],
           A[12],     A[13],    A[14],  A[15]]
    return C



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
    # print("Rotation ux, uy, uz, alpha): \t", posArray[3], # unrounded
    #                                    '\t', posArray[4],
    #                                    '\t', posArray[5],
    #                                    '\t', posArray[6])