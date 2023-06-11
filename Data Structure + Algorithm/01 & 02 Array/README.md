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

# Two Pointers

There are several ways to implement two-pointers. To start, let's look at the following method:

Start the pointers at the edges of the input. Move them towards each other until they meet.

Converting this idea into instructions:

1. Start one pointer at the first index 0 and the other pointer at the last index input.length - 1.
2. Use a while loop until the pointers are equal to each other.
3. At each iteration of the loop, move the pointers towards each other. This means either increment the pointer that started at the first index, decrement the pointer that started at the last index, or both. Deciding which pointers to move will depend on the problem we are trying to solve.

Here's some pseudocode illustrating the concept:

```
function fn(arr):
    left = 0
    right = arr.length - 1

    while left < right:
        Do some logic here depending on the problem
        Do some more logic here to decide on one of the following:
            1. left++
            2. right--
            3. Both left++ and right--
```

Example 1: Given a string s, return true if it is a palindrome, false otherwise.

A string is a palindrome if it reads the same forward as backward. That means, after reversing it, it is still the same string. For example: "abcdcba", or "racecar".

```
def check_if_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True
```

Example 2: Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise. This problem is similar to Two Sum.

For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13.

```
def check_for_target(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        curr = nums[left] + nums[right]
        if curr == target:
            return True
        if curr > target:
            right -= 1
        else:
            left += 1

    return False
```

# Alternative Two Pointers

Algorithms are beautiful because of how abstract they are - "two pointers" is just an idea, and it can be implemented in many ways. Let's look at another method. The following method is applicable when the problem has two iterables in the input, for example, two arrays.

**Move along both inputs simultaneously until all elements have been checked.**

Converting this idea into instructions:

1. Create two pointers, one for each iterable. Each pointer should start at the first index.
2. Use a while loop until one of the pointers reaches the end of its iterable.
3. At each iteration of the loop, move the pointers forward. This means incrementing either one of the pointers or both of the pointers. Deciding which pointers to move will depend on the problem we are trying to solve.
4. Because our while loop will stop when one of the pointers reaches the end, the other pointer will not be at the end of its respective iterable when the loop finishes. Sometimes, we need to iterate through all elements - if this is the case, you will need to write extra code here to make sure both iterables are exhausted.

Here's some pseudocode illustrating the concept:

```
function fn(arr1, arr2):
    i = j = 0
    while i < arr1.length AND j < arr2.length:
        Do some logic here depending on the problem
        Do some more logic here to decide on one of the following:
            1. i++
            2. j++
            3. Both i++ and j++

    // Step 4: make sure both iterables are exhausted
    // Note that only one of these loops would run
    while i < arr1.length:
        Do some logic here depending on the problem
        i++

    while j < arr2.length:
        Do some logic here depending on the problem
        j++
```

Example 3: Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.

```
def combine(arr1, arr2):
    ans = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1

    while i < len(arr1):
        ans.append(arr1[i])
        i += 1

    while j < len(arr2):
        ans.append(arr2[j])
        j += 1

    return ans
```

Example 4: 392. Is Subsequence.

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a sequence of characters that can be obtained by deleting some (or none) of the characters from the original string, while maintaining the relative order of the remaining characters. For example, "ace" is a subsequence of "abcde" while "aec" is not.

```
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)
```

# Sliding Window

Sliding window is another common approach to solving problems related to arrays. A sliding window is actually implemented using two pointers! Before we start, we need to talk about the concept of a subarray.

Given an array, a subarray is a contiguous section of the array. All the elements must be adjacent to each other in the original array and in their original order. For example, with the array [1, 2, 3, 4], the subarrays (grouped by length) are:

[1], [2], [3], [4]

[1, 2], [2, 3], [3, 4]

[1, 2, 3], [2, 3, 4]

[1, 2, 3, 4]

**A subarray can be defined by two indices, the start and end.**

Here's some pseudocode that puts it all together:

```
function fn(nums, k):
    left = 0
    curr = 0
    answer = 0
    for (int right = 0; right < nums.length; right++):
        curr += nums[right]
        while (curr > k):
            curr -= nums[left]
            left++

        answer = max(answer, right - left + 1)

    return answer
```

Example 1: Given an array of positive integers nums and an integer k, find the length of the longest subarray whose sum is less than or equal to k. This is the problem we have been talking about above. We will now formally solve it.

To summarize what each variable does in the code:

- left: the leftmost index of our current window
- right: the rightmost index of our current window
- curr: the sum of our current window
- ans: the length of the longest valid window we have seen so far

```
def find_length(nums, k):
    left = curr = ans = 0
    for right in range(len(nums)):
        curr += nums[right]
        while curr > k:
            curr -= nums[left]
            left += 1
        ans = max(ans, right - left + 1)

    return ans
```

Example 2: You are given a binary substring s (a string containing only "0" and "1"). You may choose up to one "0" and flip it to a "1". What is the length of the longest substring achievable that contains only "1"?

For example, given s = "1101100111", the answer is 5. If you perform the flip at index 2, the string becomes 1111100111.

```
def find_length(s):
    left = curr = ans = 0
    for right in range(len(s)):
        if s[right] == "0":
            curr += 1
        while curr > 1:
            if s[left] == "0":
                curr -= 1
            left += 1
        ans = max(ans, right - left + 1)

    return ans
```

Example 3: 713. Subarray Product Less Than K.

Given an array of positive integers nums and an integer k, return the number of subarrays where the product of all the elements in the subarray is strictly less than k.

For example, given the input nums = [10, 5, 2, 6], k = 100, the answer is 8. The subarrays with products less than k are:

[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]

```
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        ans = left = 0
        curr = 1

        for right in range(len(nums)):
            curr *= nums[right]
            while curr >= k:
                curr //= nums[left]
                left += 1
            ans += right - left + 1

        return ans
```

# Prefix Sum

When a subarray starts at index 0, it is considered a "prefix" of the array. A prefix sum represents the sum of all prefixes.

Prefix sum is a technique that can be used on arrays (of numbers). The idea is to create an array prefix where prefix[i] is the sum of all elements up to the index i (inclusive). For example, given nums = [5, 2, 1, 6, 3, 8], we would have prefix = [5, 7, 8, 14, 17, 25].

Prefix sums allow us to find the sum of any subarray in O(1). If we want the sum of the subarray from i to j (inclusive), then the answer is prefix[j] - prefix[i - 1], or prefix[j] - prefix[i] + nums[i] if you don't want to deal with the out of bounds case when i = 0.

Building a prefix sum is very simple. Here's some pseudocode:

```
Given an array nums,

prefix = [nums[0]]
for (int i = 1; i < nums.length; i++)
    prefix.append(nums[i] + prefix[prefix.length - 1])
```
