import unittest

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    quicksort(input_list)

    first_number, second_number = '', ''

    while input_list:
        first_number += str(input_list.pop()) if input_list else ''
        second_number += str(input_list.pop()) if input_list else ''

    return [int(first_number), int(second_number)]
    
def quicksort(items):
    # Applies quick sort to items
    sort_elements(items, 0, len(items) - 1)

def sort_elements(items, begin_index, end_index):
    # Base case
    if end_index <= begin_index:
        return
    # Pick pivot element and pre-sort items
    pivot_index = pick_pivot_and_presort(items, begin_index, end_index)
    # Sort left-handed elements of pivot
    sort_elements(items, begin_index, pivot_index - 1)
    # Sort right-handed elements of pivot
    sort_elements(items, pivot_index + 1, end_index)

def pick_pivot_and_presort(items, begin_index, end_index):    
    left_index = begin_index
    pivot_index = end_index
    pivot_value = items[pivot_index]
    # Check if left-handed element smaller or greater than pivot
    while (pivot_index != left_index):
        left_item = items[left_index]
        if left_item <= pivot_value:
            left_index += 1
            continue
        # Move left-handed elements greater than pivot to right 
        items[left_index] = items[pivot_index - 1]
        items[pivot_index - 1] = pivot_value
        items[pivot_index] = left_item
        pivot_index -= 1
    
    return pivot_index



class TestRearrangeElements(unittest.TestCase):
    """docstring for TestRearrangeElements"""
    def test_one(self):
        print("\n##### Test case 1: test input_list with uneven number of elements #####")
        input_list = [1, 2, 3, 4, 5]
        solution = [542, 31]
        self.run_test(input_list, solution)
        pass

    def test_two(self):
        print("\n##### Test case 2: test input_list with even number of elements #####")
        input_list = [4, 6, 2, 5, 9, 8]
        solution = [964, 852]
        self.run_test(input_list, solution)
        pass

    def run_test(self, input_list, solution):
        print("Input list: {}".format(input_list))
        print("Expected result: {}".format(solution))
        result = rearrange_digits(input_list)
        self.assertEqual(self.cross_sum(result), self.cross_sum(solution))
        print("Actual result: {}".format(result))

    def cross_sum(self, number_list):
        cross_sum = 0
        for number in number_list:
            cross_sum += number
        return cross_sum

        
