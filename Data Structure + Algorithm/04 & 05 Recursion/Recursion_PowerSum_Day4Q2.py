"""
Given a peculiar type of array in which each element is either an integer 
or another peculiar array.
Assume that a peculiar array is never empty.

Write a function that will take a peculiar array as its input 
and find the sum of its elements.

If an array is an element in the peculiar array 
you have to convert it to its equivalent value 
so that you can sum it with the other elements.

Example 1:

Input: [2,3,[4,1,2]]
Output: 2+3+(4+1+2)^2 = 54

Example 2:

Input: [1,2,[7,[3,4],2]]
Output: 1+2+(7+(3+4)^3+2)^2 = 123907
"""

def power_sum(array,power=1):
    sum = 0
    for i in array:
        if type(i) == list:
            sum += power_sum(i, power+1)
        else:
            sum += i
    return sum**power


print(54, power_sum([2,3,[4,1,2]]))
print(123907, power_sum([1,2,[7,[3,4],2]]))
print(116, power_sum([1,2,[3,4],[[2]]]))