import math


class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y


class Point_3D:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z


def point_distance(a, b):
	if type(a) != Point or type(b) != Point:
		print("Needs Point class format for both points")
		raise TypeError
	return math.sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2))


def point_distance_3d(a, b):
	if type(a) != Point_3D or type(b) != Point_3D:
		print("Needs Point_3D class format for both points")
		raise TypeError
	return math.sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2) + pow(a.z - b.z, 2))
