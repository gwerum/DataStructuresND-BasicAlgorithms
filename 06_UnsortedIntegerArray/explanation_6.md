## Explanation for find_min_max.py

### Task
The task is to implement a method, which finds the minimum and maximum element of an unsorted array in a single traversal.

### Code explanation

Starting the traversal, the current minimum and maximum values are initialized with the value of the first element of the unsorted array. In the following traversal the min and max values are compared in each step with the value of the current element. If the current value is greater respectively smaller then max or min, those values are updated. 

---

### Runtime efficiency

Both tasks described in the previous section, finding the pivot element and finding the target element, use a binary search approach, which has a time complexity of order O(log(n)). Adding both up leaves us still with time complexity O(log(n)).

|  | Time complexity |
| ------------------- | --------------- |
| **get_min_max(ints)** | O(n) |

**n**: number of elements in *ints*

---

### Test Cases

Three test cases have been implemented to test the method `get_min_max(ints)`:

1. **Test 1: Positive integers 0 to 100**: Finds min and max element in unsorted array containg positive integers in the range 0 to 100.
2. **Test 2: Negative & Positive integers -100 to 100**: Finds min and max element in unsorted array containg negative & positive integers in the range -100 to 100.
3. **Test 3: Invalid input**: Tests if function correctly detects invalid input.

The test cases can be executed using the following command:

```
python -m unittest find_min_max.py
```