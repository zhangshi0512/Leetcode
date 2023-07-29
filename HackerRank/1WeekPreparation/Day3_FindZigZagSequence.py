"""
Given an array of n distinct integers, transform the array into a zig zag sequence 
by permuting the array elements. 
A sequence will be called a zig zag sequence 
if the first k elements in the sequence are in increasing order 
and the last k elements are in decreasing order, where k = (n+1)/2. 
You need to find the lexicographically smallest zig zag sequence of the given array.

Example
a = [2,3,5,1,4]
Now if we permute the array as [1,4,5,3,2], the result is a zig zag sequence.
"""


def findZigZagSequence(a, n):
    a.sort()  # 对数组进行排序
    # 找到中间元素的索引，需要注意的是，我们希望中间元素是递增序列的最后一个元素，所以这里使用 (n - 1) / 2
    mid = int((n - 1)/2)

    # 交换中间元素和最后一个元素
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1  # 定义开始位置
    ed = n - 2  # 定义结束位置

    # 当开始位置小于等于结束位置时，交换开始位置和结束位置的元素
    while (st <= ed):  # 注意这里的条件是小于等于
        a[st], a[ed] = a[ed], a[st]
        st = st + 1  # 将开始位置向右移动
        ed = ed - 1  # 将结束位置向左移动

    # 打印结果
    for i in range(n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end=' ')
    return


print([1, 2, 3, 7, 6, 5, 4], findZigZagSequence([1, 2, 3, 4, 5, 6, 7], 7))
