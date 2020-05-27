## Explanation for square_root.py

### Code explanation

The task of this exercise is to implement a method, which computes the square root of a number. Only the floor value of the square root needs to be computed. Two boundary conditions were given:

1. For implementation of the method no Python library such as math or similar shall be used.
2. The method shall have time complexity of no more than `O(log(n))`.

To satisfy the second boundary condition some kind of binary search approach is required. The square root **r** of a number **n** will be somewhere in the range `0 <= s < n`. To find the square root in an efficient manner, this range be recursively searched, splitting the range in half during each recursion.

---

### Runtime efficiency

As described in the previous section, the solution space for the square root **s** will be searched with a binary search approach, reducing the solution space by half during each recursion. 

Therefore, considering the initial solution space to be input size **n** (`0 <= s < n`), the square root **r** can be found with `O(log(n))`.

---

### Test Cases

Three test cases have been implemented in `class TestSquareRoot()` for the following default and corner use cases:

1. **Test 1: integers**: the square root of all integers from 0 to 100 are computed & tested.
2. **Test 2: floats**: the square root of 100 random floats in the range from 0 to 100 are computed & tested.
3. **Test 3: runtime test**: A simple runtime test by computing the square root of integers from single digit size to an integer with 31 digits is executed. From comparing the runtimes, the *O(log(n))* time complexity can be numerically shown.

The test cases can be executed using the following command:

```
python -m unittest square_root.py
```