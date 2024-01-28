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

### Divide and Conquer: Inversion Counting and Order Statistics

When both subarrays (left `L` and right `R`) are sorted, we can count cross inversions where an element in `L` is greater than an element in `R`.

For two sorted subarrays `L` and `R`:

L: [1, 2, 4, ...] R: [3, 5, 6, ...]

If `L[i] > R[j]`, all subsequent elements in `L` form inversions with `R[j]`.

To count cross inversions:

```plaintext
cross_inversion(L[1...n], R[1...m]) {
    z = 0;
    for i = 1 to n {
        for j = 1 to m {
            if (L[i] > R[j]) {
                z += (n - i + 1);
                break; // All subsequent elements in L will also be greater
            }
        }
    }
    return z;
}
```

#### Merge Sort and Inversion Counting

The function `count_inversion` counts the total number of inversions in an array by dividing it into halves and recursively counting inversions in each half and cross inversions.

```plaintext
count_inversion(A[1...n]) {
    if (n <= 1) return 0;
    X = count_inversion(A[1...n/2]);
    Y = count_inversion(A[n/2+1...n]);
    sort(A[1...n/2]);
    sort(A[n/2+1...n]);
    Z = cross_inversion(A[1...n/2], A[n/2+1...n]);
    return X + Y + Z;
}
```

#### Complexity Analysis

The recurrence for this divide and conquer approach is:

```plaintext
T(n) = 2 * T(n/2) + n * log(n)
```

An approximation for the upper bound is:

```plaintext
T(n) = 2 * T(n/2) + n * 1.01
```

Implying that \( T(n) = O(n^{1.01}) \), a slightly superlinear complexity.

#### Visual Representation of Recurrence

The recurrence for the divide and conquer approach can be visualized as a binary tree where each node represents a subproblem size and the cost of combining solutions.

```plaintext
         T(n)
         /  \
   T(n/2)    T(n/2)
   /  \        /  \
T(n/4) T(n/4) T(n/4) T(n/4)
```

Each level of the tree represents a halving of the problem size, and the work done at each level is proportional to the number of subproblems multiplied by the cost to combine them.

## Order Statistics

Finding the k-th smallest element in an unsorted array is a classic problem known as order statistics.

```plaintext
A: [1, ... , n] k: n/2
```

For example, to find the median, which is the 50th percentile, we can use a divide and conquer approach similar to Quick Sort, which is more efficient than sorting the entire array.
