def power_sum(array,power=1):
    sum = 0
    for i in array:
        if type(i) == list:
            sum += power_sum(i, power+1)
        else:
            sum += i
    return sum**power


print(power_sum([1,2,[3,4],[[2]]]))