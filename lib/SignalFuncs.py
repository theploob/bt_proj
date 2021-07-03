import math
import scipy.special
import scipy.constants

sqrt2 = math.sqrt(2)
frequency = 2450000000  # 2.45Gz bluetooth frequency
friis_const = 20 * math.log10(4 * math.pi / scipy.constants.c)  # ~-147.552216




# Calculates the path-loss constant from a distance and a signal strength
def calc_pl_constant(d, s):
	return s / (10 * math.log10(d))


def reverse_path_loss(d):
	if d <= 1:
		return -1
	return -60 - 10 * 2.6 * math.log10(d)


# Calculates the Friis free-space path-loss at distance d
# Uses global frequency, changeable through change_freq()
def calc_friis_pl_constant(d):
	global frequency
	global friis_const
	return 20 * math.log10(d) + 20 * math.log10(frequency) + friis_const


def change_freq(f):
	global frequency
	frequency = f


# For the given accuracy value and sigma, calculate the acceptable dB range (+/-)
# Takes accuracy between 0 and 1, sigma
def valid_db_range(accuracy, sigma):
	if 0 < accuracy < 1:
		return sigma * sqrt2 * scipy.special.erfcinv(2 - 2 * accuracy)
	else:
		print("Tried to acquire a dB range with accuracy not between 0 and 1")
		raise ValueError
