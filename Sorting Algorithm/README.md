Sorting Algorithms

[Sorting Algorithms - Geeksforgeeks](https://www.geeksforgeeks.org/sorting-algorithms/#)

Table for the complexity comparison:

| Name                 | Best Case | Average Case | Worst Case | Memory | Stable | Method Used         |
| -------------------- | --------- | ------------ | ---------- | ------ | ------ | ------------------- |
| Quick Sort           | n log n   | n log n      | n^2 log n  | No     | No     | Partitioning        |
| Merge Sort           | n log n   | n log n      | n log n    | n      | Yes    | Merging             |
| Heap Sort            | n log n   | n log n      | n log n    | 1      | No     | Selection           |
| Insertion Sort       | n         | n^2          | n^2        | 1      | Yes    | Insertion           |
| Tim Sort             | n         | n log n      | n log n    | n      | Yes    | Insertion & Merging |
| Selection Sort       | n^2       | n^2          | n^2        | 1      | No     | Selection           |
| Shell Sort           | n log n   | n^(4/3)      | n^(3/2)    | 1      | No     | Insertion           |
| Bubble Sort          | n         | n^2          | n^2        | 1      | Yes    | Exchanging          |
| Tree Sort            | n log n   | n log n      | n log n    | n      | Yes    | Insertion           |
| Cycle Sort           | n^2       | n^2          | n^2        | 1      | No     | Selection           |
| Strand Sort          | n         | n^2          | n^2        | n      | Yes    | Selection           |
| Cocktail Shaker Sort | n         | n^2          | n^2        | 1      | Yes    | Exchanging          |
| Comb Sort            | n log n   | n^2          | n^2        | 1      | No     | Exchanging          |
| Gnome Sort           | n         | n^2          | n^2        | 1      | Yes    | Exchanging          |
| Odd–even Sort        | n         | n^2          | n^2        | 1      | Yes    | Exchanging          |

---

### Sorting Algorithms Overview

- **Merge Sort**

  - Time Complexity: \( O(n \log n) \)
  - Space Complexity: \( O(n) \)

- **Quick Sort**

  - Time Complexity: \( O(n \log n)^2 \)
  - Space Complexity: \( O(\log n)^2 \)

- **Heap Sort**

  - Time Complexity: \( O(n \log n) \)
  - Space Complexity: \( O(\log n) \)

- **Counting Sort**

  - Time Complexity: \( O(n+k) \)
  - Space Complexity: \( O(k) \)

- **Radix Sort**
  - Time Complexity: \( O(nk) \)
  - Space Complexity: \( O(n+k) \)

### Merge Sort Explanation

- An array \( A \) with elements \( A[1] \) to \( A[n] \) is considered.
- The approach follows a divide and conquer strategy to reduce the problem size.
  - The array is divided into two halves, \( A[1 \ldots \frac{n}{2}] \) and \( A[\frac{n}{2} + 1 \ldots n] \).
- Then Merge the sorted array back

```python
merge(A[1,...,n], B[1,...,m]) {
    C[1,...,n+m],
    i=j=k=1;
    while(i<=n && j<=m) {
        if(A[i] <= B[j]) {
            C[k] = A[i],
            i++, k++;
        } else {
            C[k] = B[j],
            j++, k++;
        }
    }
    if(i<=n) C[k:] = A[i:];
    if(j<=m) C[k:] = B[j:];
    return C;
}
```

- Time Complexity for merge function: O(n+m)

- Merge Sort Algorithm Complete Process:

```python
merge_sort(A[...n]) {
    if (n < 2) return A;
    left = merge_sort(A[1 : n/2]);
    right = merge_sort(A[n/2 + 1 : n]);
    return merge(left, right);
}
```

- T(n) = 2T(n/2) + n
- **Recurrence Relation for Merge Sort:**

  - \( T(n) = 2T(\frac{n}{2}) + n \)
  - \( a = 2, b = 2, c = 1 \)
  - \( T(n) = \Theta(n \log n) \)

- **Space Complexity for Merge Sort:**
  - \( S(n) = \Theta(n) \)
  - Note: Not in-place; needs an array to merge and copy over.

**Derivation of Time Complexity:**

- \( n + \frac{n}{2} + \frac{n}{4} + \frac{n}{8} + ... + \frac{n}{2^{\log n}} \)
- Summed up equals: \( n(1 + \frac{1}{2} + \frac{1}{4} + ... + \frac{1}{2^{\log n}}) \)
- Which simplifies to: \( \Theta(n \log n) \)

### Quick Sort Algorithm

#### Quick Sort Overview

- Relies on **Partitioning**
- **Pivot** is a number in A
- A[1...n]

```plaintext
Quick-Sort(A[1...n]) {
    if (n < 2) return A;
    pivot_index = Partition(A[1...n]);
    Quick-Sort(A[1 : pivot_index-1]);
    Quick-Sort(A[pivot_index+1 : n]);
}
```

#### Time Complexity Analysis

- Best case: \( T(n) = 2T(\frac{n}{2}) + n \), which simplifies to \( \Theta(n \log n) \)
- Worst case: \( T(n) = T(\frac{n}{3}) + T(\frac{2n}{3}) + n \)
- Bounds: \( \frac{n \log n}{3} \leq T(n) \leq n \log \frac{3n}{2} \)

The notes include graphical representations of the partitioning concept and the recursive nature of the quick sort algorithm, illustrating the divide-and-conquer approach and how the partition sizes change.

Now, let's transcribe the content from the fifth page `Sorting I_Page_05.png`.

### Quick Sort Algorithm Continued

#### Partitioning in Quick Sort

```plaintext
Partition(A[1...n]) {
    Pivot = A[n];
    i = 0; // i = -1 if starting from index 0
    for (curr = 1; curr <= n-1; curr++) {
        if (A[curr] <= Pivot) {
            Swap(A[curr], A[i+1]);
            i++;
        }
    }
    Swap(A[n], A[i+1]);
    return i+1;
}
```

- Time Complexity for partition function: \( T(n) = O(n) \)
- Space Complexity for partition function: \( S(n) = O(1) \)

#### First Version of Partitioning

- Choose pivot as the last number.
- Procedure includes:
  1. If the current element is greater than the pivot, increment the current pointer.
  2. If the current element is less than or equal to the pivot, swap with the element at the incrementing index.

The notes also contain an example illustrating the partitioning process within an array, showing how elements are swapped based on their comparison with the pivot.

```
Example:
Array A = [10, 2, 3, 7, 8, 9, 4, 6]

Partitioning steps:
1. Pivot chosen is the last element, A[7] = 6.
2. Initialization: i points to the start of the array, curr is the current index starting from A[1].

During partitioning:
- Elements less than or equal to pivot (6) are moved to the left of the pivot.
- Elements greater than pivot are kept on the right.

After partitioning:
- The pivot (6) is placed after all elements smaller than or equal to it.
- The array is now partially sorted around the pivot.

Resulting array:
- Elements to the left of the pivot are less than or equal to 6.
- Elements to the right of the pivot are greater than 6.

```

### Quick Sort Algorithm - Detailed Partition Function

#### Partition Function Code

```plaintext
Partition(A[1...n]) {
    Pivot = A[n];
    i = 0; // i = -1 if starting from index 0
    for (curr = 1; curr <= n-1; curr++) {
        if (A[curr] <= Pivot) {
            Swap(A[curr], A[i+1]);
            i++;
        }
    }
    Swap(A[n], A[i+1]);
    return i+1;
}
```

##### Time and Space Complexity for Partition Function

- \( T(n) = \Theta(n) \)
- \( S(n) = \Theta(1) \)
- Note: Quick Sort is an in-place sort.

- The notes emphasize the in-place nature of Quick Sort and provide detailed steps for the partition function, which is central to the Quick Sort algorithm. The function swaps elements in the array based on their comparison to the pivot value, and rearranges the array so that elements less than the pivot are on the left and elements greater than the pivot are on the right.

---
