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

---
