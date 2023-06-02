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
