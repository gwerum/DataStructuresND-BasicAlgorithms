from random import randint, uniform
import unittest

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    for index, integer in enumerate(ints):
        if type(integer) == int:
            if index == 0:
                min_element, max_element = integer, integer
            else:
                if integer < min_element:
                    min_element = integer
                if integer > max_element:
                    max_element = integer
        else:
            raise ValueError("Error: No integer array provided as argument.")

    return min_element, max_element

class TestMinMax(unittest.TestCase):
    """docstring for TestMinMax"""
    def test_range_0_100(self):
        print("\n##### Test case 1: integers between 0 and 100 #####")
        _input = [randint(0,100) for i in range(20)]
        self.run_test(_input)

    def test_range_m100_100(self):
        print("\n##### Test case 2: integers between -100 and 100 #####")
        _input = [randint(-100,100) for i in range(20)]
        self.run_test(_input)

    def test_invalid_input(self):
        print("\n##### Test case 3: float list as input #####")
        _input = [uniform(-100.0,100.0) for i in range(20)]
        print("Input array:")
        print(_input)
        print("Expected result: ValueError")
        with self.assertRaises(ValueError):
            get_min_max(_input)
        eval_str = "'get_min_max()' correctly raises ValueError"
        print("Actual result: {}".format(eval_str))
        
    def run_test(self, _input):
        print("Input array:")
        print(_input)
        expected_result = (min(_input), max(_input))
        actual_result = get_min_max(_input)
        print("Expected result: {}".format(expected_result))
        print("Actual result: {}".format(actual_result))
        self.assertEqual(get_min_max(_input), expected_result)