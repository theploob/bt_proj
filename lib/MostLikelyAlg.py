import Point
import SignalFuncs

# List of anchor Points
bluetooth_anchors = []


# Calculate the matrix of theoretical rssi
# Takes x dimension, y dimension
def calculate_theoretical_rssi_matrix(x_dim, y_dim):
	expected_rssi = [[[0 for z in range(0, len(bluetooth_anchors))] for y in range(0, y_dim)] for x in range(0, x_dim)]
	for x in range(0, x_dim):
		for y in range(0, y_dim):
			for z in range(0, len(bluetooth_anchors)):
				pass


# Set the bluetooth anchors to the given list of anchors
# Takes a list of Point.Point
def set_anchors(anchors):
	global bluetooth_anchors
	if type(anchors) != list:
		raise TypeError
	if type(anchors[0]) != Point.Point:
		raise TypeError
	bluetooth_anchors = anchors


# Add an anchor to the list of bluetooth anchors
# Takes a Point.Point
def add_anchor(anchor):
	global bluetooth_anchors
	if type(anchor) != Point.Point:
		raise TypeError
	bluetooth_anchors.append(anchor)


# Print the matrix of expected rssi values
# Format is [x][y][values]
def print_rssi_expected(vals):
	x_dim = len(vals)
	y_dim = len(vals[0])
	z_dim = len(vals[0][0])

	for x in range(0, x_dim):
		for y in range(0, y_dim):
			print("[", end='')
			for z in range(0, z_dim):
				print("%0.3f" % (vals[x][y][z]), end='')
				if z != z_dim - 1:
					print(", ", end='')
			print("]    ", end='')
		print('')


# Print the score matrix
# Format is [x][y]
def print_score_matrix(vals):
	x_dim = len(vals)
	y_dim = len(vals[0])

	for x in range(0, x_dim):
		for y in range(0, y_dim):
			print("%d" % vals[x][y], end='')
		print('')
