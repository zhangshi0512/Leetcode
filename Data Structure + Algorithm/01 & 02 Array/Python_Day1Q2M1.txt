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
