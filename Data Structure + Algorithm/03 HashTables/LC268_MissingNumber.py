"""
268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, 
so all numbers are in the range [0,3]. 
2 is the missing number in the range since it does not appear in nums.

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, 
so all numbers are in the range [0,2]. 
2 is the missing number in the range since it does not appear in nums.

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, 
so all numbers are in the range [0,9]. 
8 is the missing number in the range since it does not appear in nums.

Constraints:

n == nums.length
1 <= n <= 10^4
0 <= nums[i] <= n
All the numbers of nums are unique.
"""


def missingNumber(nums):
    n = len(nums)
    full_nums = []
    for i in range(n+1):
        full_nums.append(i)

    for num in nums:
        full_nums.remove(num)

    for last_num in full_nums:
        return last_num


print(2, missingNumber([3, 0, 1]))
print(8, missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print()


def missingNumber2(nums):
    n = len(nums)
    sum_n = (n*(n+1))//2

    return sum_n - sum(nums)


print(2, missingNumber2([3, 0, 1]))
print(8, missingNumber2([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print()


def missingNumber3(nums):
    missing = len(nums)
    for i, num in enumerate(nums):
        missing ^= i ^ num
    return missing


print(2, missingNumber3([3, 0, 1]))
print(8, missingNumber3([9, 6, 4, 2, 3, 5, 7, 0, 1]))
