# Time = O(nlogn)  Space = O(n)
def sorted_squared(array):
    new_array = [0]*len(array)
    for i in range(len(array)):
        new_array[i] = array[i]**2
        # new_array[i] = array[i]*array[i]
    new_array.sort()
    return new_array


print(sorted_squared([-5, 1, 2]))
print(sorted_squared([0, 1, 2]))
print(sorted_squared([]))
