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

# 插入排序包含两个主要步骤：迭代和交换。

# 先说迭代：
# 从数组的第二个元素开始，我们对每个元素进行迭代。
# 对于每个元素，我们都要通过交换将其放入正确的位置。

# 再说交换：
# 我们不断地将当前元素与其前一个元素进行比较，如果当前元素较小，则交换它们的位置。
# 这个过程一直持续到我们找到一个元素小于或等于当前元素，或者我们到达数组的开头。

# 所以在最坏情况下，对于一个包含N个元素的数组，插入排序所需要的最长步骤是N次迭代和N(N-1)/2次交换。

# 随着N的增长，插入排序的效率用大O表示是O(N^2)。因此它并不高效。
