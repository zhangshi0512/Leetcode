def two_sum_optimal(array,target):
    num_available = {}
    for i in range(len(array)):
        needed_val = target - array[i]
        if needed_val in num_available:
            return [i,num_available[needed_val]]
        else:
            num_available[array[i]]=i
    return []


print(two_sum_optimal([2,-1,5,3],4))

