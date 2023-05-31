# Big O Analysis

Here's a table with common operations on arrays in Python along with their corresponding time and space complexity in terms of Big O notation:

| Operation           | Time Complexity (Big O) | Space Complexity (Big O) |
| ------------------- | ----------------------- | ------------------------ |
| Access by Index     | O(1)                    | O(1)                     |
| Search              | O(n)                    | O(1)                     |
| Insert at End       | O(1)                    | O(1)                     |
| Insert at Beginning | O(n)                    | O(n)                     |
| Insert at Middle    | O(n)                    | O(n)                     |
| Delete at End       | O(1)                    | O(1)                     |
| Delete at Beginning | O(n)                    | O(n)                     |
| Delete at Middle    | O(n)                    | O(n)                     |
| Resize              | O(n)                    | O(n)                     |
| Copy                | O(n)                    | O(n)                     |
| Sort                | O(n log n)              | O(n) or O(log n)         |
| Reverse             | O(n)                    | O(1)                     |
| Concatenate         | O(n)                    | O(n)                     |
| Slicing             | O(k)                    | O(k)                     |

Note:

- "n" represents the number of elements in the array.
- "k" represents the length of the resulting slice.

Keep in mind that these complexities are general estimates and may vary depending on the specific implementation and data structures used in Python.

# Array Methods

Here's a table that includes some common array methods in Python, along with a column that demonstrates the usage of each method using short code examples:

| Method    | Description                                                   | Example Code                   |
| --------- | ------------------------------------------------------------- | ------------------------------ |
| append()  | Adds an element to the end of the array.                      | `arr.append(5)`                |
| insert()  | Inserts an element at a specific index.                       | `arr.insert(2, 7)`             |
| extend()  | Appends elements from an iterable to the end of the array.    | `arr.extend([8, 9, 10])`       |
| remove()  | Removes the first occurrence of an element from the array.    | `arr.remove(3)`                |
| pop()     | Removes and returns an element at a specific index.           | `removed_element = arr.pop(2)` |
| index()   | Returns the index of the first occurrence of an element.      | `index = arr.index(4)`         |
| count()   | Returns the number of occurrences of an element in the array. | `count = arr.count(2)`         |
| sort()    | Sorts the elements of the array in ascending order.           | `arr.sort()`                   |
| reverse() | Reverses the order of the elements in the array.              | `arr.reverse()`                |
| copy()    | Returns a shallow copy of the array.                          | `arr_copy = arr.copy()`        |
| clear()   | Removes all elements from the array.                          | `arr.clear()`                  |
| len()     | Returns the number of elements in the array.                  | `length = len(arr)`            |
| slice()   | Returns a new array with elements from a specified slice.     | `new_arr = arr[1:4]`           |

Note: `arr` represents the name of the array. Make sure to replace it with your actual array variable name in the code examples.

Remember to consult the Python documentation for a comprehensive list of array methods and their usage.
