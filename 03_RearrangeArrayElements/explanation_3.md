## Explanation for rearrange_elements.py

### Task

The task of this exercise is to implement a method, which rearranges the elements of an array such that its elements form two integer numbers who's cross sum is the maximum of all possible combinations using all elements. The following example illustrates it with an example:
```
input_array = [3, 1, 5, 4, 2]
solution = [542, 31] or [531, 42]
```
The following boundary conditions are given:
1. The input array is generally unsorted.
2. The input array can be of arbitrary size.
3. The array contains single digit integer elements only.
4. The solution shall have time complexity no larger than **O(nlog(n))**.
5. Python built-in sorting functions are not allowed to be used.

---

### Code explanation

Solving the task requires picking all elements from the array and forming two new integers. Yielding the maximum cross-sum is achieved by the following considerations:

1. The first digit of each resulting integer has the highest contribution to the cross-sum. Thus, the largest integers from the input array should be chosen for the first digits.
2. The two resulting (multi-digit) integers should be in best case of equal digit size. Thus, the method will return two multi-digit integers, whose number of digits is the same (if the array contains an even number of elements) or differs by one digit only (if the array contains an uneven number of elements).

Picking the largest elements first for the first digits requires sorting of the input array. To achieve this in *O(nlog(n))* a quick sort has been implemented.

Once, the input array is sorted, solving the task is pretty straight-forward:
1. Pick the largest element for the first digit of *number one*.
2. Pick the second largest element for the first digit of *number two*.
3. Pick the third largest element for the second digit of *number one*.

&nbsp;&nbsp;&nbsp;...

&nbsp;&nbsp;&nbsp;N-1: Pick the second smallest element for the last digit of *number one*.<br/>
&nbsp;&nbsp;&nbsp;N: Pick the smallest element for the last digit of *number two*.

---

### Runtime efficiency

As described above, solving the task consists of two main steps: sorting the input array and picking all elements from the sorted array starting from largest to smallest.

|  | Time complexity |
| ------------------- | --------------- |
| **quicksort(*input_array*)** | O(nlog(n)) |
| **rearrange_digits(*sorted_array*)** | O(n) |
| **Total** | **O(nlog(n) + n) ~ O(nlog(n))** |

**n**: number of elements in *input_array*

---

### Test Cases

Three test cases have been implemented to test the method `rearrange_digits(input_list)` for the following default and corner use cases:

1. **Test 1: Default use cases**: Rearranges elements of integer arrays of even and uneven size to yield maximum cross-sum.
2. **Test 2: Multi-digit inputs**: Rearranges elements of integer arrays of with multi-digit elements to yield maximum cross-sum.
3. **Test 3: invalid input**: Checks if the method correctly detects invalid input.

The test cases can be executed using the following command:

```
python -m unittest rearrange_elements.py
```