"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, 
return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

def longestConsecutive(nums):
    # If the array is empty, return 0
    if not nums:
        return 0

    # Use a HashSet to remove duplicates and for efficient lookups
    num_set = set(nums)

    # Initialize the longest streak
    long_streak = 0

    # Iterate through each number in the set
    for num in num_set:
        # If this number is the first in a sequence (i.e., num - 1 is not in the set),
        # then test this sequence for the longest streak
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Continue adding to the streak until we reach a number that isn't in the set
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            # Update the longest streak
            long_streak = max(long_streak, current_streak)

    return long_streak

# Time Complexity: O(n). Although the contents of the for loop run in O(n) time, 
# every element is visited inside the for loop only once. So in total, the time complexity is O(n).
# Space Complexity: O(n), because the worst case scenario is the set containing all the elements in the array.

print(4, longestConsecutive([100,4,200,1,3,2]))
print(9, longestConsecutive([0,3,7,2,5,8,4,6,0,1]))