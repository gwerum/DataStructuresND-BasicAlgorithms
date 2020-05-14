import unittest

def rotated_array_search(input_list, target):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), target(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    pivot_index = find_pivot_index_of(input_list)
    # If no pivot found, search sorted array
    if pivot_index == None:
        return binary_search(input_list, target), pivot_index
    # If array detected not sorted, skip search
    if pivot_index == -1:
        return -1, pivot_index
    # Check if pivot is target, else make binary search on respective section
    if target == input_list[pivot_index]:
        return pivot_index
    elif target < input_list[0]:
        start = (pivot_index+1)
        return binary_search(input_list[start:], target, start), pivot_index
    else:
        end = (pivot_index+1)
        return binary_search(input_list[:(end+1)], target), pivot_index
  
def find_pivot_index_of(array, start_index=0):
    """
    Finds the pivot point of a rotated & sorted array.

    Args:
        array(array), start_index(int): Input array and start_index of original array (first recursion)
    Returns:
        None: if not pivot is found
        -1: if array is detected to be unsorted
    """
    # Base case
    if len(array) == 1: 
        return None
    # Check if pivot index close to mid index
    mid_index = (len(array)-1) // 2
    if array[mid_index] > array[mid_index + 1]:
        if array_is_sorted(array, mid_index):
            return start_index + mid_index
        return -1
    if array[mid_index] < array[mid_index - 1]:
        if array_is_sorted(array, (mid_index-1)):
            return start_index + (mid_index-1)
        return -1
    # Search pivot in unsorted section
    if array[0] >= array[mid_index]:
        _unsorted, _sorted = array[:mid_index+1], array[mid_index+1:]
        return find_pivot_index_of(_unsorted)
    else:
        _unsorted, _sorted = array[mid_index+1:], array[:mid_index+1]
        return find_pivot_index_of(_unsorted, mid_index + 1)

def array_is_sorted(array, pivot):
    first, second = array[0:pivot+1], array[pivot+1:]
    return (first == sorted(first)) and (second == sorted(second))

def binary_search(array, target, start_index=0):
    """
    Implements standard binary search for array
    """
    mid_index = (len(array)-1) // 2
    # Base case
    if array[mid_index] == target:
        return start_index + mid_index
    if len(array) == 1:
        return -1
    # Recurse over target half
    if target > array[mid_index]:
        return binary_search(array[(mid_index+1):], target, start_index+mid_index+1)
    else:
        return binary_search(array[:(mid_index+1)], target, start_index)

def linear_search(input_list, target):
    for index, element in enumerate(input_list):
        if element == target:
            return index
    return -1


class TestRotatedSearch(unittest.TestCase):
    """docstring for TestRotatedSearch"""
    def test_1(self):
        print("\n######### Test case 1: Rotated & sorted array ######### ")
        input_list = [6, 7, 8, 9, 10, 11, 12, 13, 14, 1, 2, 3, 4]
        targets = list(range(-2,8))
        for target in targets:
            self.run_test(input_list, target)

    def test_2(self):
        print("\n######### Test case 2: Rotated & unsorted array ######### ")
        input_list = [6, 7, 8, 1, 2, 5, 3, 4]
        targets = list(range(-2,3))
        for target in targets:
            self.run_test(input_list, target)

    def test_3(self):
        print("\n######### Test case 3: Not rotated & sorted array ######### ")
        input_list = list(range(15))
        targets = list(range(12,17))
        for target in targets:
            self.run_test(input_list, target)

    def run_test(self, input_list, target):
        print("\nInput list: {}".format(input_list))
        print("Search value: {}".format(target))
        actual_result, pivot = rotated_array_search(input_list, target)
        expected_result = linear_search(input_list, target)
        print("Pivot Index: {}".format(pivot))
        if pivot == -1: # Array not sorted
            expected_result = -1
            self.assertEqual(actual_result, expected_result)
        else:
            self.assertEqual(actual_result, expected_result)
        print("Expected result: {}".format(expected_result))
        print("Actual result: {}".format(actual_result))



