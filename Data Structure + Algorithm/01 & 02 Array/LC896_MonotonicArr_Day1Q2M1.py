"""
896. Monotonic Array

An array is monotonic if it is either monotone increasing 
or monotone decreasing.

An array nums is monotone increasing if for all 
i <= j, nums[i] <= nums[j]. 
An array nums is monotone decreasing if for all 
i <= j, nums[i] >= nums[j].

Given an integer array nums, 
return true if the given array is monotonic, 
or false otherwise.
"""

def monotonic_array(array):
    first = array[0]
    last = array[len(array)-1]
    if first > last:
        for i in range(len(array)-1):
            if array[i] < array[i+1]:
                return False
    elif first == last:
        for i in range(len(array)-1):
            if array[i] != array[i+1]:
                return False
    else:
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                return False
    return True


print(monotonic_array([1]))
