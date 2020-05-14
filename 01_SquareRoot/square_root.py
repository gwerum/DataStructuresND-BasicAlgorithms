import unittest
import math
import random
import time

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    return sqrt_floor(int(number), 0, int(number))


def sqrt_floor(square, start, end):
	if (square == 0 or square == 1):
		return square
	# Base case
	root_guess = (start + end) // 2
	if root_guess == start:
		return root_guess
	# Use binary search to recursively find sqare root
	square_guess = root_guess**2
	if square_guess == square:
		return root_guess
	elif square_guess > square:
		return sqrt_floor(square, start, root_guess)
	else:
		return sqrt_floor(square, root_guess, end)


class TestSquareRoot(unittest.TestCase):
	"""docstring for TestSquareRoot"""
	def test_integers(self):
		print("\n######### Test case 1: test integer numbers from 0 to 100 ######### ")
		integers = list(range(0,100))
		self.run_test(integers)

	def test_floats(self):
		print("\n######### Test case 2: test float numbers from 0 to 100 ######### ")
		floats = [round(random.uniform(0,100), 3) for _ in range(0,100)]
		self.run_test(floats)

	def test_time_complexity(self):
		print("\n######### Test case 3: test execution time ######### ")
		numbers = [0,1,12,1234**2,123456**2,12345678**2,12345678910**2,1234567891011**2,1234567891011121**2]
		exec_time = []
		for idx, number in enumerate(numbers):
			print("\nComputing sqare root of {}".format(number))
			start_time = time.time()
			actual_result = sqrt(number)
			exec_time.append(time.time() - start_time)
			self.assertEqual(actual_result, math.floor(math.sqrt(number)))
			print("Result: {}".format(actual_result))
			print("Execution time: {} seconds".format("{:.8f}".format(exec_time[-1])))

	def run_test(self, test_input):
		print("\nInput:\n {}".format(test_input))
		expected_result, actual_result = [], []
		for number in test_input:
			expected_result.append(math.floor(math.sqrt(number)))
			actual_result.append(sqrt(number))
			self.assertEqual(actual_result[-1], expected_result[-1])
		print("\nExpected result:\n {}".format(expected_result))
		print("\nActual result:\n {}".format(actual_result))



