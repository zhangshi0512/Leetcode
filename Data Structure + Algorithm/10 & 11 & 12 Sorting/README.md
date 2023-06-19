# Big O Analysis

Here a complexity comparison for these sorting algorithms. Please note that the stability and method used (comparison-based or non-comparison-based) are typically independent of the best, average, and worst case scenario. Also, the space complexity is generally noted as additional memory required beyond input storage:

| Algorithm       | Best Case   | Average Case            | Worst Case    | Memory    | Stable | Method Used      |
| --------------- | ----------- | ----------------------- | ------------- | --------- | ------ | ---------------- |
| Selection Sort  | Θ(n²)       | Θ(n²)                   | Θ(n²)         | Θ(1)      | No     | Comparison-based |
| Bubble Sort     | Θ(n)        | Θ(n²)                   | Θ(n²)         | Θ(1)      | Yes    | Comparison-based |
| Insertion Sort  | Θ(n)        | Θ(n²)                   | Θ(n²)         | Θ(1)      | Yes    | Comparison-based |
| Merge Sort      | Θ(n log(n)) | Θ(n log(n))             | Θ(n log(n))   | Θ(n)      | Yes    | Comparison-based |
| Quick Sort      | Θ(n log(n)) | Θ(n log(n))             | Θ(n²)         | Θ(log(n)) | No     | Comparison-based |
| Heap Sort       | Θ(n log(n)) | Θ(n log(n))             | Θ(n log(n))   | Θ(1)      | No     | Comparison-based |
| Counting Sort   | Θ(n + k)    | Θ(n + k)                | Θ(n + k)      | Θ(k)      | Yes    | Non-comparison   |
| Radix Sort      | Θ(nk)       | Θ(nk)                   | Θ(nk)         | Θ(n + k)  | Yes    | Non-comparison   |
| Bucket Sort     | Θ(n + k)    | Θ(n + k)                | Θ(n²)         | Θ(n)      | Yes    | Non-comparison   |
| Bingo Sort      | Θ(n)        | Θ(n²)                   | Θ(n²)         | Θ(1)      | Yes    | Comparison-based |
| Shell Sort      | Θ(n log(n)) | depends on gap sequence | Θ(n(log(n))²) | Θ(1)      | No     | Comparison-based |
| Tim Sort        | Θ(n)        | Θ(n log(n))             | Θ(n log(n))   | Θ(n)      | Yes    | Comparison-based |
| Comb Sort       | Θ(n log(n)) | Θ(n²)                   | Θ(n²)         | Θ(1)      | No     | Comparison-based |
| Pigeonhole Sort | Θ(n + k)    | Θ(n + k)                | Θ(n + k)      | Θ(n + k)  | Yes    | Non-comparison   |

Please note that:

- n is the number of elements to be sorted.
- k is the range of input.
- "Best Case" refers to the performance of the algorithm when the input is already sorted.
- "Average Case" refers to the performance of the algorithm under a random permutation of input.
- "Worst Case" refers to the performance of the algorithm when the input is reverse sorted.
- "Memory" refers to the additional space

# Code Template

Here are the Python code snippets with comments:

1. **Selection Sort (选择排序):**

```python
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
```

2. **Bubble Sort (冒泡排序):**

```python
def bubble_sort(arr):
    n = len(arr)
    # 遍历数组所有元素
    for i in range(n):
        # 最后i个元素已在位，所以内部循环到n-i-1
        for j in range(0, n-i-1):
            # 如果当前元素大于下一个，就交换位置
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr  # 返回排序后的数组
```

3. **Insertion Sort (插入排序):**

```python
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
```

4. **Merge Sort (归并排序):**

```python
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
```

5. **Quick Sort (快速排序):**

```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # 选择一个基准元素
        pivot = arr[0]
        # 分割数组为两个子数组，小于等于基准元素的放在左边，大于基准元素的放在右边
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        # 递归地对子数组进行快速排序
        return quicksort(left) + [pivot] + quicksort(right)

```
