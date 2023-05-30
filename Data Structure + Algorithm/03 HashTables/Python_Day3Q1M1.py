# Brute Force Solution
def two_sum(array,target):
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            if array[i]+array[j] == target:
                return [i,j]
    return []


print(two_sum([2,-1,5,3],4))