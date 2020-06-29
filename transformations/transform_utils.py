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
	return [0, 0, 0, tx,
			0, 0, 0, ty,
			0, 0, 0, tz,
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


# TODO
def decodeMatrix(m, verbose):

	tx = 0
	ty = 0
	tz = 0
	x = 0
	y = 0
	z = 0
	w = 0

	if (verbose):
		print("Translation:", tx, ty, tz)
		print("Rotation:", x, y, z, w)
	return[tx, ty, tz, x, y, z, w]


#############################################
#                                           #
#          General Helper Functions         #
#                                           #
#############################################

def prettyPrintMatrix(x):
	col = math.sqrt(len(x))
	for i in range(0, len(x)):
		if (i%col == 0):
			print()
		print(x[i], end='          ')
	print()