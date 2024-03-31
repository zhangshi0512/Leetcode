# Graph

## Definition of a Graph:

A graph G is defined as G = (V, E) where:

- V: set of vertices
- E: set of edges

### Directed Graph Example:

```plaintext
Directed Graph G1:
Vertices V = {1, 2, 3, 4, 5}
Edges E = {(1,2), (1,3), (2,3), (3,5), (4,2), (4,3), (5,4)}
```

### Undirected Graph Example:

```plaintext
Undirected Graph G2:
Vertices V = {1, 2, 3, 4}
Edges E = {(1,2), (2,1), (1,3), (3,1)}
```

## Graph Representation:

1. **Adjacency List**

   - Example for vertex 1: [2] -> [3]
   - Example for vertex 2: [1] -> [3]
   - Example for vertex 3: [1] -> [2] -> [5]
   - Example for vertex 4: [...]

2. **Adjacency Matrix**
   - Example Matrix A for vertices 1 to 4:

```markdown
|     | 1   | 2   | 3   | 4   |
| --- | --- | --- | --- | --- |
| 1   | T   | T   | T   | F   |
| 2   | T   | F   | T   | F   |
| 3   | T   | T   | F   | F   |
| 4   | F   | T   | F   | F   |
```

Where T = true if `(u,v) ∈ E` and F = false otherwise.

---

## Space Complexity for Graph Representation:

Assuming a graph with |V| = n and |E| = m.

- **Adjacency List**: O(n + m) space
- **Adjacency Matrix**: O(n^2) space

Note:

- Self-loops are not allowed in class examples.
- Self-loops are allowed outside of class.

For the number of edges, we have:

- 0 ≤ m ≤ n^2
- For m = Ω(n^2), the graph is dense.
- For m = O(n), the graph is sparse.

## Operations for Graph Representations:

- **For Adjacency List**: Designed for operations that traverse neighbors.
- **For Adjacency Matrix**: Designed to determine if `(u, v) ∈ E`.

---
