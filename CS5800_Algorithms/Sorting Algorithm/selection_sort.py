"""
Selection Sort (选择排序):

Time Complexity:
Best Case: Θ(n²)
Average Case: Θ(n²)
Worst Case: Θ(n²)
Space Complexity: Θ(1)
"""

def selection_sort(arr):
    # 遍历数组所有元素
    for i in range(len(arr)):
        # 找出剩余未排序部分的最小元素
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # 交换找到的最小元素和未排序部分的第一个元素
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr  # 返回排序后的数组

# 选择排序主要包括两个步骤：查找和交换。

# 先说查找：
# 对于包含N个元素的数组，我们首先找到最小元素的位置。
# 查找需要比较N-1次。

# 再说交换：
# 我们将找到的最小元素与第一个元素交换位置。
# 对于第二个元素，我们再找到剩余数组中的最小元素，将其与第二个元素交换。

# 所以总共需要N-1次交换。

# 所以在最坏情况下，对于一个包含N个元素的数组，选择排序所需要的最长步骤是N-1次交换和N-1次比较。

# 随着N的增长，选择排序的效率用大O表示是O(N^2)。因此它并不高效。

ol1 = [4, 2, 7, 1, 3]
ol2 = [65, 55, 45, 35, 25, 15, 10]

print(ol1)
print(selection_sort(ol1))
print()
print(ol2)
print(selection_sort(ol2))