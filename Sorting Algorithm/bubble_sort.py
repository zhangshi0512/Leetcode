"""
Bubble Sort (冒泡排序):

Time Complexity:
Best Case: Θ(n)
Average Case: Θ(n²)
Worst Case: Θ(n²)
Space Complexity: Θ(1)
"""

def bubble_sort(lis):
    unsorted_until_index = len(lis)-1 #该索引之前的数据都没排过序
    isSorted = False
    
    while not isSorted: #除非数组排好了序，否则不会停下来
        isSorted = True #终止条件， 当不发生交换则数组完成排序为True
        for i in range(unsorted_until_index):
            if lis[i] > lis[i+1]: #如果出现交换，则完成排序的条件为False
                isSorted = False
                lis[i], lis[i+1] = lis[i+1], lis[i]
        unsorted_until_index = unsorted_until_index - 1 #每一轮交换完成后未排序索引前进一位
        
    return lis

# 冒泡排序的执行步骤分为两种：比较和交换

# 先说比较
# 对于包含N个元素的数组，第一轮为N-1对元素进行了N-1次比较
# 第二轮是N-2次比较，第三轮是N-3次比较……
# 因此总共需要 （N-1） + （N-2） + （N-3） + …… + 1 次比较

# 再讲交换
# 最坏的情况不是乱序，而是完全反序
# 在最坏情况下每次比较后都得进行一次交换

# 所以在最坏情况下，对于一个包含N个元素的数组
# 用冒泡排序所需要的最长步骤是 2 * （ （N-1） + （N-2） + （N-3） + …… + 1 ）
# 随着N的增长，冒泡排序的效率用大O表示是O(N^2)
# 因此它并不高效
        
ol1 = [4, 2, 7, 1, 3]
ol2 = [65, 55, 45, 35, 25, 15, 10]

print(ol1)
print(bubble_sort(ol1))
print()
print(ol2)
print(bubble_sort(ol2))