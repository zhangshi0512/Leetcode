# Big O Analysis

Here's a table listing the common operations for hash tables in Python, along with their corresponding time and space complexity:

| Operation     | Time Complexity (Average Case) | Time Complexity (Worst Case) | Space Complexity |
| ------------- | ------------------------------ | ---------------------------- | ---------------- |
| Insertion     | O(1)                           | O(n)                         | O(n)             |
| Deletion      | O(1)                           | O(n)                         | O(n)             |
| Access/Search | O(1)                           | O(n)                         | O(n)             |
| Update        | O(1)                           | O(n)                         | O(n)             |
| Check Size    | O(1)                           | O(1)                         | O(1)             |
| Iteration     | O(n)                           | O(n)                         | O(n)             |

Explanation:

- Time Complexity (Average Case): This refers to the average time complexity of the operation when the hash table is evenly distributed. It assumes that the hash function provides a good distribution of keys.
- Time Complexity (Worst Case): This represents the worst-case time complexity of the operation when there are collisions or other unfavorable conditions.
- Space Complexity: This indicates the additional space required by the hash table to store the key-value pairs.

Here's a brief explanation of each operation:

1. Insertion: Adding a new key-value pair to the hash table.
2. Deletion: Removing a key-value pair from the hash table.
3. Access/Search: Retrieving the value associated with a specific key or searching for a key in the hash table.
4. Update: Modifying the value associated with a specific key in the hash table.
5. Check Size: Determining the number of key-value pairs stored in the hash table.
6. Iteration: Visiting each key-value pair in the hash table.

It's important to note that the time and space complexity can vary based on factors such as the load factor (the ratio of filled slots to the total number of slots) and the underlying implementation of the hash table. The complexities mentioned in the table represent the typical performance characteristics for hash tables.

# Hash Table Methods

Here's a table listing the commonly used hash table methods in Python, along with a column that includes a short code demonstration:

| Method              | Description                                                                                | Code Demo                                        |
| ------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------ |
| `dict()`            | Creates a new empty dictionary/hash table.                                                 | `my_dict = dict()`                               |
| `clear()`           | Removes all key-value pairs from the dictionary.                                           | `my_dict.clear()`                                |
| `copy()`            | Returns a shallow copy of the dictionary.                                                  | `new_dict = my_dict.copy()`                      |
| `get(key)`          | Returns the value associated with a given key.                                             | `value = my_dict.get(key)`                       |
| `items()`           | Returns a list of all key-value pairs in the dictionary.                                   | `key_value_pairs = my_dict.items()`              |
| `keys()`            | Returns a list of all keys in the dictionary.                                              | `keys_list = my_dict.keys()`                     |
| `values()`          | Returns a list of all values in the dictionary.                                            | `values_list = my_dict.values()`                 |
| `pop(key)`          | Removes and returns the value associated with a key.                                       | `value = my_dict.pop(key)`                       |
| `popitem()`         | Removes and returns a random key-value pair.                                               | `key, value = my_dict.popitem()`                 |
| `setdefault(key)`   | Returns the value associated with a key or sets a default value if the key is not present. | `value = my_dict.setdefault(key, default_value)` |
| `update(dict)`      | Updates the dictionary with key-value pairs from another dictionary.                       | `my_dict.update(other_dict)`                     |
| `__contains__(key)` | Checks if a key exists in the dictionary.                                                  | `if key in my_dict:`                             |

Please note that the code demonstrations are simplified examples and may require appropriate initialization of the `my_dict` and `key` variables.

These are some of the most commonly used methods for hash tables in Python. Each method serves a different purpose and provides flexibility in manipulating the key-value pairs stored in the dictionary.

## dict vs default dict

Here's a comparison table showcasing the methods of the Python `dict` class and the `defaultdict` class from the `collections` module, along with a short code demo for each method:

| Method                          | `dict`                                                                                                                                   | `defaultdict`                                                                                                                                                      |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `dict[key]`                     | Returns the value associated with `key` in the dictionary.                                                                               | Returns the value associated with `key` in the dictionary, or the default value if the key is not present.                                                         |
| `dict.get(key, default)`        | Returns the value associated with `key` in the dictionary. If `key` is not found, returns `default`.                                     | Returns the value associated with `key` in the dictionary. If `key` is not found, returns the default value for the specified data type.                           |
| `dict[key] = value`             | Assigns `value` to `key` in the dictionary, overwriting any previous value.                                                              | Assigns `value` to `key` in the dictionary, overwriting any previous value.                                                                                        |
| `del dict[key]`                 | Removes `key` and its associated value from the dictionary.                                                                              | Removes `key` and its associated value from the dictionary.                                                                                                        |
| `dict.keys()`                   | Returns a list of all the keys in the dictionary.                                                                                        | Returns a list of all the keys in the dictionary.                                                                                                                  |
| `dict.values()`                 | Returns a list of all the values in the dictionary.                                                                                      | Returns a list of all the values in the dictionary.                                                                                                                |
| `dict.items()`                  | Returns a list of all key-value pairs in the dictionary as tuples.                                                                       | Returns a list of all key-value pairs in the dictionary as tuples.                                                                                                 |
| `dict.clear()`                  | Removes all the key-value pairs from the dictionary.                                                                                     | Removes all the key-value pairs from the dictionary.                                                                                                               |
| `len(dict)`                     | Returns the number of key-value pairs in the dictionary.                                                                                 | Returns the number of key-value pairs in the dictionary.                                                                                                           |
| `defaultdict[key]`              | Returns the value associated with `key` in the dictionary. If `key` is not found, returns the default value for the specified data type. | Returns the value associated with `key` in the dictionary. If `key` is not found, creates a new key-value pair with the default value for the specified data type. |
| `defaultdict.get(key, default)` | Returns the value associated with `key` in the dictionary. If `key` is not found, returns `default`.                                     | Returns the value associated with `key` in the dictionary. If `key` is not found, returns the default value for the specified data type.                           |
| `defaultdict[key] = value`      | Assigns `value` to `key` in the dictionary, overwriting any previous value.                                                              | Assigns `value` to `key` in the dictionary, overwriting any previous value.                                                                                        |
| `del defaultdict[key]`          | Removes `key` and its associated value from the dictionary.                                                                              | Removes `key` and its associated value from the dictionary.                                                                                                        |
| `defaultdict.keys()`            | Returns a list of all the keys in the dictionary.                                                                                        | Returns a list of all the keys in the dictionary.                                                                                                                  |
| `defaultdict.values()`          | Returns a list of all the values in the dictionary.                                                                                      | Returns a list of all the values in the dictionary.                                                                                                                |
| `defaultdict.items()`           | Returns a list of all key-value pairs in the dictionary as tuples.                                                                       | Returns a list of all key-value pairs in the dictionary as tuples.                                                                                                 |
| `defaultdict.clear()`           | Removes all the key-value pairs from the dictionary.                                                                                     | Removes all the key-value pairs from the dictionary.                                                                                                               |
| `len(defaultdict)`              | Returns the number of key-value pairs in the dictionary.                                                                                 | Returns the number of key-value pairs in the dictionary.                                                                                                           |

Here's a short code demo illustrating the usage of these methods:

```python
from collections import defaultdict

# Python dictionary
my_dict = {
    'apple': 3,
    'banana': 5,
}

print(my_dict['apple'])  # Output: 3
print(my_dict.get('banana', 0))  # Output: 5
my_dict['orange'] = 2
print(my_dict)  # Output: {'apple': 3, 'banana': 5, 'orange': 2}
del my_dict['banana']
print(my_dict)  # Output: {'apple': 3, 'orange': 2}
print(list(my_dict.keys()))  # Output: ['apple', 'orange']
print(list(my_dict.values()))  # Output: [3, 2]
print(list(my_dict.items()))  # Output: [('apple', 3), ('orange', 2)]
my_dict.clear()
print(my_dict)  # Output: {}

# defaultdict
my_defaultdict = defaultdict(int)
print(my_defaultdict['apple'])  # Output: 0
print(my_defaultdict.get('banana', 0))  # Output: 0
my_defaultdict['orange'] = 2
print(my_defaultdict)  # Output: defaultdict(<class 'int'>, {'apple': 0, 'orange': 2})
del my_defaultdict['apple']
print(my_defaultdict)  # Output: defaultdict(<class 'int'>, {'orange': 2})
print(list(my_defaultdict.keys()))  # Output: ['orange']
print(list(my_defaultdict.values()))  # Output: [2]
print(list(my_defaultdict.items()))  # Output: [('orange', 2)]
my_defaultdict.clear()
print(my_defaultdict)  # Output: defaultdict(<class 'int'>, {})
```

In the above code, both `my_dict` and `my_defaultdict` are initialized as empty dictionaries. The code demonstrates various dictionary operations such as accessing values, adding and removing key-value pairs, and retrieving keys, values, and items. The `defaultdict` is instantiated with an `int` factory, which sets the default value for any non-existing key to zero.
