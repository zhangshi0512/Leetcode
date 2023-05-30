def max_area(array):
    max_area = 0
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            area = min(array[i],array[j])*(j-i)
            max_area = max(max_area,area)
    return max_area


print(max_area([3,7,5,6,8,4]))