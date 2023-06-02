"""
Insertion Sort (插入排序):

Time Complexity:
Best Case: Θ(n)
Average Case: Θ(n²)
Worst Case: Θ(n²)
Space Complexity: Θ(1)
"""

def insertion_sort(arr):
    # 遍历从1到len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        # 将arr[0..i-1]中大于key的元素向后移一位
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr  # 返回排序后的数组
