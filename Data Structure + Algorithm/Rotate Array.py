def rotate_array(k, array):
  if k==0 or len(array)==0:
    return array
  else:
    k = k%len(array)
    subarraykeep = array[:-k]
    subarrayrotate = array[-k:]
    subarrayrotate.extend(subarraykeep)
    return subarrayrotate

print(rotate_array(3, [1,2,3,4]))
print(rotate_array(2, [1,2]))
print(rotate_array(2, [-1,-100,3,99]))
print(rotate_array(3, [1,2,3,4,5,6,7]))