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
    if len(nums) <= 1:
        return len(nums)

    # Sort the array
    nums.sort()

    # Initialize variables
    longest = 1
    current = 1

    # Iterate through the array, starting from the second element
    for i in range(1, len(nums)):
        # If the current number is equal to 
        # the previous number + 1, increment the current streak
        if nums[i] == nums[i-1] + 1:
            current += 1
        # If the current number is equal to the previous number, 
        # skip this iteration
        elif nums[i] == nums[i-1]:
            continue
        # Otherwise, reset the current streak
        else:
            current = 1
        # Update the longest streak
        longest = max(longest, current)
        
    return longest


print(4, longestConsecutive([100,4,200,1,3,2]))
print(9, longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
