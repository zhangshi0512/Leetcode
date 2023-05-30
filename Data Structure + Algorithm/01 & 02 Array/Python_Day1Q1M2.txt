# Time = O(n) Space = O(n)
def sorted_squared(array):
    i = 0
    j = len(array) - 1
    new_array = [0] * len(array)
    for k in reversed(range(len(array))):
        sq_i = array[i]**2
        sq_j = array[j]** 2
        if sq_i > sq_j:
            new_array[k] = sq_i
            i += 1
        else:
            new_array[k] = sq_j
            j -= 1
    return new_array


print(sorted_squared([-5,-4,-2, 1, 9,12]))
