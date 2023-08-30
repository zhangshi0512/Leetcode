"""
Given an array of integers and a target value, 
determine the number of pairs of array elements that have a difference equal to the target value. 

Example k = 1, arr = [1, 2, 3, 4], k = 2-1 = 3-2 = 4-3 , so it should return 3. 
Example k = 2, arr = [1, 5, 3, 4, 2], k = 3-1 = 4-2 = 5-3, so it should return 3.
"""

###
# Convert the given array into a set for O(1) lookups.
# Traverse through the array. For each element,
# check if element + k exists in the set.
# If yes, then it's a valid pair. Increment the count.
# Return the count at the end.
###


def pairs(k, arr):
    # Convert the array to a set for O(1) lookups
    arr_set = set(arr)

    count = 0
    for num in arr:
        # Check if num + k exists in the set
        if num + k in arr_set:
            count += 1

    return count


print(3, pairs(1, [1, 2, 3, 4]))
print(3, pairs(2, [1, 5, 3, 4, 2]))
