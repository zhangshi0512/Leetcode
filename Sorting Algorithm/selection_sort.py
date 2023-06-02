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
