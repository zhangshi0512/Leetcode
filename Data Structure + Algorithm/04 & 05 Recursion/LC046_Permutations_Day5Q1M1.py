"""
46. Permutations

Given an array nums of distinct integers, 
return all the possible permutations. 
You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""

def all_permutations(nums):
    # set up the empty list for results
        permutations = []
        # resolve the empty nums scenario
        if len(nums)==0:
            return permutations.append(nums)

        # set up i, j. 
        # i used to iterate through entire array for the begining number
        # j used to swap the numbers after the beginning number
        def helper(nums, i):
            # when i iterated to the last number in the array,
            # append the copy of that output array
            if i == len(nums) - 1:
                permutations.append(nums[:])
                return
            # for each i, iterate j to get the following numbers swapped.
            # The order for recursion is: 
            # 1. swap
            # 2. recursion for i = i + 1
            # 3. swap
            #*4. i will be stopped once it reaches len(nums)-1
            for j in range(i,len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                helper(nums, i+1)
                nums[i], nums[j] = nums[j], nums[i]

        helper(nums, 0)
        return permutations


array = [1,2,3]
print(all_permutations(array))
