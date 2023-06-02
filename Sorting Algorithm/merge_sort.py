"""
Merge Sort (归并排序):

Time Complexity:
Best Case: Θ(n log(n))
Average Case: Θ(n log(n))
Worst Case: Θ(n log(n))
Space Complexity: Θ(n) (Merge sort requires a temporary array to merge the sorted halves)
"""

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        # 分别对每半部分进行递归
        merge_sort(left)
        merge_sort(right)
        # 用于遍历两半部分的两个迭代器
        i = 0
        j = 0
        # 用于主列表的迭代器
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # 使用了左半部分的值
                arr[k] = left[i]
                # 向前移动迭代器
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            # 移动到下一个插槽
            k += 1
        # 所有剩余值
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr  # 返回排序后的数组

# 归并排序的主要步骤包括分解、排序和合并。

# 先说分解：
# 我们将数组一直分解到只有一个元素，这个元素本身就是有序的。

# 再说排序和合并：
# 然后，我们开始合并这些子数组，以产生排序后的较大的子数组，直到整个数组排序完成。

# 在这个过程中，我们需要额外的空间来存储临时的合并数组。

# 所以在最坏情况下，对于一个包含N个元素的数组，归并排序所需要的最长步骤是N log(N)次操作。

# 随着N的增长，归并排序的效率用大O表示是O(N log(N))，这比前面的O(N^2)要高效得多。

# 但是，由于其需要额外的存储空间，所以空间复杂性为O(N)。
