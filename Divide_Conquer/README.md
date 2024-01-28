# Divide and Conquer Algorithms

This section covers two fundamental divide and conquer algorithms, Merge Sort and Quick Sort, and introduces a divide and conquer strategy for counting inversions in an array.

## Merge Sort

Merge Sort divides an array into two halves, sorts each half, and then merges them back together.

```
[First Half] [Second Half]
```

## Quick Sort

Quick Sort partitions an array around a pivot, then sorts the subarrays formed to the left and right of the pivot.

```
[<Pivot] [Pivot] [>Pivot]
```

## Counting Inversions

An inversion in an array is a situation where two elements are out of their natural order, i.e., a pair `(i, j)` such that `i < j` and `A[i] > A[j]`.

### Brute Force Method

The brute force method iterates through each element pair and counts the inversions, with a time complexity of \( O(n^2) \).

```plaintext
cnt = 0;
for (i = 1 to n) {
    for (j = i + 1 to n) {
        if (A[i] > A[j]) {
            cnt++;
        }
    }
}
return cnt;
```

### Divide and Conquer Strategy

By dividing the array and counting inversions within each part and across the parts, we can achieve more efficient counting, with a time complexity of \( O(n \log n) \), similar to merge sort.

- Inversions within each part are counted during the sorting process.
- Cross inversions are counted when merging the two sorted halves.

The total inversions are the sum of left inversions, right inversions, and cross inversions. This is optimally done during the merge step of the Merge Sort algorithm.

Example for clarity:

```plaintext
Array A: [1, 4, 3, 5, 2]
Left Inversions: (4, 3)
Right Inversions: (5, 2)
Cross Inversions: Computed during merge step
```

The process of counting inversions can be incorporated into the merge step of the Merge Sort algorithm, allowing us to sort the array and count inversions simultaneously.
