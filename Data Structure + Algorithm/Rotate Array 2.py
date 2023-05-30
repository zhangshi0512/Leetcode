def reverse(array,start,end):
    while(start<end):
        array[start],array[end] = array[end], array[start]
        start +=1
        end -=1
    return array

def rotate_array(k, array):
    k= k % len(array)
    reverse(array, 0, len(array)-1)
    reverse(array, 0, k-1)
    reverse(array, k, len(array)-1)
    return array

print(rotate_array(3, [1,2,3,4]))
print(rotate_array(2, [1,2]))
print(rotate_array(2, [-1,-100,3,99]))
print(rotate_array(3, [1,2,3,4,5,6,7]))