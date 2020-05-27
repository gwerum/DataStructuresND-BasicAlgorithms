## Explanation for rotated_search.py

### Task

The task of this exercise is to implement a method, which finds the index of an element with a given value in a rotated, but sorted array. The method shall have a time complexity of no more than `O(log(n))`.

A rotated, sorted array means: the element with the smallest value is not located at the start (or end) index of the array, but can have an arbitrary index, depending on how often the array has been rotated. For example, the following (ordered) *numbers* array has been rotated three times to the left:

```
numbers = [4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
```

---

### Code explanation
Finding the element with time complexity O(log(n)) requires using binary search instead of linear search. Binary search can only be applied to unrotated, sorted arrays (trees, lists, ...), thus, the following two steps are required for implementation:

1. **Find the pivot point**: use a binary search approach to find the index of the pivot element of the rotated array.
2. **Search target in sorted section**: Knowing the pivot index leaves us with two sorted sections of the array. By comparing with the target the section containing the solution space can be selected and searched with a standard binary search.

A nice explanation of the problem can be found at: https://stackoverflow.com/questions/4773807/searching-in-a-sorted-and-rotated-array

---

### Runtime efficiency

Both tasks described in the previous section, finding the pivot element and finding the target element, use a binary search approach, which has a time complexity of order O(log(n)). Adding both up leaves us still with time complexity `O(log(n))`.

|  | Time complexity | Space complexity |
| ------------------- | --------------- | ---------------- |
| **find_pivot_index_of(*array*)** | O(log(n)) | O(1) |
| **rotated_array_search(*input_list,target*)** | O(log(n)) | O(1) |
| **Total** | O(2log(n)) ~ **O(log(n))** | **O(1)** |

**n**: number of elements in *input_list*

---

### Test Cases

Three test cases have been implemented to test the method `rotated_array_search(input_list, target)` for the following default and corner use cases:

1. **Test 1: Rotated & Sorted input_list**: Searches for existing and non-existing elements in a rotated & sorted input_list.
2. **Test 2: Rotated & unsorted input_list**: Searches for existing and non-existing elements in a rotated & unsorted input_list. Test checks if unsorted input_list is detected correctly.
3. **Test 3: Not rotated, but sorted input_list**: Searches for existing and non-existing elements in a not rotated & sorted input_list. Test checks if index of target element is still returned even though the input_list is not rotated.

The test cases can be executed using the following command:

```
python -m unittest rotated_search.py
```