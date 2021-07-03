import lib.SignalFuncs as SignalFuncs
import lib.Point as Point

beacon1 = Point.Point(0,0)
beacon2 = Point.Point(10,10)
beacon3 = Point.Point(10,0)
beacon4 = Point.Point(0,8)
beaconList = [beacon1, beacon2, beacon3, beacon4]

sample_readings = [-78, -82, -71, -78]

expected_rssi = [[[0 for z in range(0, 4)] for x in range(0, 5)] for y in range(0, 5)]
score_matrix = [[[0 for z in range(0, 4)] for x in range(0, 5)] for y in range(0, 5)]


def print_rssi_expected(vals):
	x_dim = len(vals)
	y_dim = len(vals[0])
	z_dim = len(vals[0][0])

	for y in range(0, y_dim):
		for x in range(0, x_dim):
			print("[", end='')
			for z in range(0, z_dim):
				print("%0.2f" % (expected_rssi[x][y][z]), end='')
				if z != z_dim - 1:
					print(", ", end='')
			print("]    ", end='')
		print('')


def print_score_matrix(vals):
	x_dim = len(vals)
	y_dim = len(vals[0])

	for y in range(0, y_dim):
		for x in range(0, x_dim):
			print("%d" % (score_matrix[y][x]), end='')
		print('')


for i in range(0, 5):  # y range
	for j in range(0, 5):  # x range
		print("Calculating theoretical rssi values for point {},{}".format(j, i))
		expected_vals = []
		for b in beaconList:
			r = SignalFuncs.reverse_path_loss(Point.point_distance(Point.Point(j, i), b))
			expected_vals.append(r)
		expected_rssi[j][i] = expected_vals

# print_rssi_expected(expected_rssi)

valid_range = SignalFuncs.valid_db_range(0.9, 4)
for i in range(0, 5):
	for j in range(0, 5):
		score = 0
		for b in range(0, 4):
			if (expected_rssi[j][i][b] - valid_range) <= sample_readings[b] <= (expected_rssi[j][i][b] + valid_range):
				score += 1
		score_matrix[j][i] = score

print_score_matrix(score_matrix)

if __name__ == "__main__":
	pass
