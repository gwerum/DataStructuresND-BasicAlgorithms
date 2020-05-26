## Explanation for sort_012.py

### Task
The task of this exercise is to implement a method, which, given an input array consisting on only 0, 1 and 2, sorts the array in a single traversal.
```
input_list = [0, 0, 2, 2, 2, 1, 1, 1, 2]
solution = [0, 0, 1, 1, 1, 2, 2, 2, 2]
```

---

### Code explanation

Implementing this method is pretty straight-forward. Knowing that the array only consists on the integers 0, 1 and 2, one can sort in a single traversal the three numbers into three seperate arrays *zeros*, *ones* and *twos*, which are concatenated after the traversal.

---

### Runtime efficiency

Both tasks described in the previous section, finding the pivot element and finding the target element, use a binary search approach, which has a time complexity of order O(log(n)). Adding both up leaves us still with time complexity O(log(n)).

|  | Time complexity |
| ------------------- | --------------- |
| **sort_012(*input_list*)** | O(n) |
| **Total** | **O(n)** |

**n**: number of elements in *input_list*

---

### Test Cases

Two test cases have been implemented to test the method `sort_012(input_list)`:

1. **Test 1: default use case**: tests the method with variable size input lists.
2. **Test 2: invalid input**: test if the method correctly detects invalid input.

The test cases can be executed using the following command:

```
python -m unittest sort_012.py
```