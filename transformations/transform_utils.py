import math

#############################################
#                                           #
#       Making Transformation Matrices      #
#                                           #
#############################################

def getTransfromMatrix(tx, ty, tz):
    return [0, 0, 0, tx,
            0, 0, 0, ty,
            0, 0, 0, tz,
            0, 0, 0, 1 ]

# TODO
def getRotationMatrix(x, y, z, w):
    return [0, 0, 0, 0,
            0, 0, 0, 0,
            0, 0, 0, 0,
            0, 0, 0, 1 ]

# TODO
def getCombinationMatrix(tx, ty, tz, x, y, z, w):
    return [0, 0, 0, tx,
            0, 0, 0, ty,
            0, 0, 0, tz,
            0, 0, 0, 1 ]

#############################################
#                                           #
#      Decoding Transformation Matrices     #
#                                           #
#############################################


# Matrix format
#   M[0]  = m11     M[1]  = m21     M[2]  = m31     M[3]  = m41
#   M[4]  = m12     M[5]  = m22     M[6]  = m32     M[7]  = m42
#   M[8]  = m13     M[9]  = m23     M[10] = m33     M[11] = m43
#   M[12] = m14     M[13] = m24     M[14] = m34     M[15] = m44

def decodeMatrix(M, verbose):

    tx = M[3]
    ty = M[7]
    tz = M[11]

    w_rad = math.acos(1 - 1/2 * (math.pow((M[9] - M[6]),2) + math.pow((M[2] - M[8]),2) + pow((M[4] - M[1]),2)))
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


def prettyPrintPosition(positionArray):
    print("Translation (x, y, z): \t\t", positionArray[0], '\t', positionArray[1], '\t', positionArray[2])
    print("Rotation (ux, uy, uz, alpha): \t", positionArray[3], '\t',  positionArray[4], '\t', positionArray[5], '\t', positionArray[6])
