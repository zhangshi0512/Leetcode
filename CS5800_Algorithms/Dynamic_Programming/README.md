# Dynamic Programming

Dynamic Programming is a method for solving complex problems by breaking them down into simpler subproblems. It is applicable to problems exhibiting the properties of overlapping subproblems and optimal substructure.

## Characteristics of Dynamic Programming:

1. **Applications**:

   - Used for optimization, counting, and feasibility problems.
   - Examples include finding the longest, maximum, or minimum subsequences or paths in data structures.

2. **Design Approach**:

   - The design often starts with a recursive algorithm that solves the problem by combining the solutions to its subproblems.

3. **Naive Recursive Implementation**:
   - A straightforward recursive implementation can lead to poor running times due to redundant calculations.

## Techniques to Improve Running Time:

To enhance the efficiency of a naive recursive algorithm, dynamic programming suggests two main approaches:

1. **Bottom-Up Approach**:

   - This approach starts solving the problem from the simplest possible subproblem and works its way up to the given problem.

2. **Top-Down Approach with Memoization**:
   - This method involves writing the recursive algorithm and storing the results of subproblems to avoid redundant work.

### Example: Longest Common Subsequence (LCS)

The LCS problem is a classic example illustrating dynamic programming. It seeks to find the longest subsequence present in two sequences.

#### Problem Statement:

- Given two sequences `A` and `B`, find the length of the longest subsequence that is common to both.

#### Example Sequences:

- Sequence `A`: [2, 3, 1, 4, 5]
- Sequence `B`: [1, 2, 3, 4, 5, 7]

#### Subsequences:

- Subsequences of `A`: [2, 4], [3, 1, 5], etc.
- Subsequences of `B`: [1, 3], [1, 4], [1, 3, 4, 5], etc.

#### Pseudocode for LCS:

```plaintext
// Function to find the LCS length
LCS(A[1..i], B[1..j]) {
    if (i == 0 || j == 0) {
        return 0; // Base case: one of the sequences is empty
    }
    if (A[i] == B[j]) {
        return 1 + LCS(A[1..i-1], B[1..j-1]); // Elements match, part of LCS
    } else {
        return max(LCS(A[1..i-1], B[1..j]), LCS(A[1..i], B[1..j-1])); // Elements don't match, find max LCS without one of the elements
    }
}
```

#### Visualization of Subproblem Dependencies:

```plaintext
// Recursive tree showing dependencies between subproblems in LCS

A[i] and B[j] subproblems:

   T(n, m)
  /      \
T(n-1, m) T(n, m-1)
/   \        /    \
...  ...    ...   ...

// T(i, j) depends on T(i-1, j) and T(i, j-1)
// Running time is exponential in terms of n and m - which is bad
```

#### Running Time Considerations:

- The naive recursive approach can potentially explore all `2^n` subsequences, which is highly inefficient.
- Dynamic programming improves this by storing the results of subproblems, reducing the running time to polynomial time.

---

I'll continue to reformat the additional handwritten notes into the README format, complete with explanations, pseudocode, and textual representations of the visuals.

---

Dynamic Programming can be implemented in two main ways: Bottom-Up and Top-Down with Memoization.

## Bottom-Up Approach

The bottom-up approach iteratively builds the solution for the smallest subproblems and then uses those solutions to construct solutions for larger subproblems.

DP Table (Initially filled with base cases)

```plaintext
+---+---+---+---+---+---+---+---+---+---+---+
|   | 0 | 1 | 2 | 3 | . | . | . | j | . | m |
+---+---+---+---+---+---+---+---+---+---+---+
| 0 | x | x | x | x | x | x | x | x | x | x |
| 1 | x |   |   |   |   |   |   |   |   |   |
| 2 | x |   |   |   |   |   |   |   |   |   |
| 3 | x |   |   |   |   |   |   |   |   |   |
| . | x |   |   |   |   |   |   |   |   |   |
| . | x |   |   |   |   |   |   |   |   |   |
| . | x |   |   |   |   |   |   |   |   |   |
| i | x |   |   |   |   |   |   |   |   |   |
| . | x |   |   |   |   |   |   |   |   |   |
| n | x |   |   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+---+---+---+
```

'x' represents base case values or previously computed values.
Blank spaces are filled iteratively from top-left to bottom-right.

In the bottom-up approach, the DP table is filled in an orderly fashion, iteratively solving each subproblem.

### Pseudocode for Bottom-Up LCS

```plaintext
// Initialize a table dp where dp[i][j] will be storing the length of LCS of A[1..i] and B[1..j].
// Note: 'n' and 'm' represent the lengths of the sequences A and B respectively.

for i from 0 to n: dp[i][0] = 0;
for j from 0 to m: dp[0][j] = 0;

for i from 1 to n:
    for j from 1 to m:
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1] + 1;
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]);

return dp[n][m]; // The length of LCS is in dp[n][m].
```

#### Complexity Analysis

- Time complexity: `O(n * m)` where `n` is the length of sequence A and `m` is the length of sequence B.
- Space complexity: `O(n * m)` for maintaining the `dp` table.

## Top-Down Approach with Memoization

The top-down approach with memoization is a recursive approach that saves the result of subproblems to avoid recomputation.

DP Table (Filled on-demand by recursive calls)

```plaintext
+---+---+---+---+---+---+---+---+---+---+---+
|   | 0 | 1 | 2 | 3 | . | . | . | j | . | m |
+---+---+---+---+---+---+---+---+---+---+---+
| 0 | x | x | x | x | x | x | x | x | x | x |
| 1 | x | / | / | / | / | / | / | / | / | / |
| 2 | x | / |   |   |   |   |   |   |   |   |
| 3 | x | / |   |   |   |   |   |   |   |   |
| . | x | / |   |   |   |   |   |   |   |   |
| . | x | / |   |   |   |   |   |   |   |   |
| . | x | / |   |   |   |   |   |   |   |   |
| i | x | / |   | / |   |   |   | / |   |   |
| . | x | / |   | / |   |   |   |   |   |   |
| n | x | / |   | / |   |   |   |   |   | / |
+---+---+---+---+---+---+---+---+---+---+---+
```

'x' represents base case values.
'/' represents values computed on-demand by recursive calls.
Blank spaces represent values not yet computed.

In the top-down approach, cells in the DP table are filled sporadically, based on the needs of the recursive calls, and the rest of the cells remain unfilled until they are needed.

This means the bottom-up fills the entire table, whereas top-down fills the table partially, just enough to compute the answer to the original problem.

### Pseudocode for Top-Down LCS with Memoization

```plaintext
// This function initializes the memoization table dp where all values are set to -1 initially.
LCS-Main(A[1..n], B[1..m]) {
    for i from 1 to n:
        for j from 1 to m:
            dp[i][j] = -1;

    return LCS(A[1..n], B[1..m], dp);
}

// Recursive function for LCS with memoization.
LCS(A[1..i], B[1..j], dp) {
    if i == 0 or j == 0:
        return 0;
    if dp[i][j] != -1:
        return dp[i][j];
    if A[i] == B[j]:
        dp[i][j] = 1 + LCS(A[1..i-1], B[1..j-1], dp);
    else:
        dp[i][j] = max(LCS(A[1..i-1], B[1..j], dp), LCS(A[1..i], B[1..j-1], dp));

    return dp[i][j];
}
```

#### Complexity Analysis

- Time complexity: `O(n * m)` since each pair `(i, j)` is solved only once due to memoization.
- Space complexity: `O(n * m)` for maintaining the `dp` table.

## Space Optimization in Dynamic Programming

For certain problems, we can optimize the space used in dynamic programming.

### Space-Optimized LCS Length

```plaintext
// Optimized space complexity for computing the length of LCS.
for i from 1 to n:
    for j from 1 to m:
        if A[i] == B[j]:
            dp[i % 2][j] = dp[(i-1) % 2][j-1] + 1;
        else:
            dp[i % 2][j] = max(dp[(i-1) % 2][j], dp[i % 2][j-1]);

return dp[n % 2][m]; // The length of LCS is in dp[n % 2][m].
```

#### Complexity Analysis

- Time complexity remains `O(n * m)`.
- Space complexity is optimized to `O(min(n, m))` by only keeping the last row of the `dp` table.

---
