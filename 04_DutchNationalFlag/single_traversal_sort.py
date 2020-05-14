import unittest

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    zeros, ones, twos = [], [], []

    input_list = input_list.copy()

    while input_list:
    	number = input_list.pop(0)
    	if number == 0:
    		zeros.append(number)
    	elif number == 1:
    		ones.append(number)
    	elif number == 2:
    		twos.append(number)
    	else:
    		raise ValueError("Error: Input_list contains elements other than 0,1,2")

    return zeros+ones+twos

class TestSingleTraversalSort(unittest.TestCase):
	"""docstring for TestSingleTraversalSort"""
	def test_default_use_case(self):
		print("\n##### Test case 1: test with valid input_list of different sizes #####")
		input_lists = [[0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2],\
					   [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1],\
					   [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]]
		for input_list in input_lists:
			self.run_test(input_list)

	def test_invalid_input(self):
		print("\n##### Test case 2: test with input_list with out-of-scope values #####")
		input_lists = [[0, 0, 2, 2, 2, 1, 1, 1, 3, 2, 0, 2],\
					   ['numbers'],\
					   [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 'O', 0, 2, 1, 0, 2, 0, 0, 1],\
					   [0, 0, 0, 0, 0, 0, 1, 1, 1, [1,0,2], 1, 1, 2, 2, 2, 2, 2, 2, 2]]
		for input_list in input_lists:
			print("\nInput list: {}".format(input_list))
			print("Expected result: Methods throws 'ValueError'")
			with self.assertRaises(ValueError):
				sort_012(input_list)
			print("Actual result: Methods correctly throws 'ValueError'")

	def run_test(self, input_list):
		print("\nInput list: {}".format(input_list))
		expected_result = sorted(input_list)
		actual_result = sort_012(input_list)
		print("Expected result: {}".format(expected_result))
		print("Actual result: {}".format(actual_result))
		self.assertEqual(actual_result, expected_result)
