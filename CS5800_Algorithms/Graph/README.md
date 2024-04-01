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

- Self-loops with two nodes are not allowed in class examples. (n->v and v->n)
- Self-loops with single node is allowed in this class. (n->n)

For the number of edges, we have:

- 0 ≤ m ≤ n^2
- For m = Ω(n^2), the graph is dense.
- For m = O(n), the graph is sparse.

## Operations for Graph Representations:

- **For Adjacency List**: Designed for operations that traverse neighbors.
- **For Adjacency Matrix**: Designed to determine if `(u, v) ∈ E`.

---

# Graph Search Algorithms: BFS and DFS

Graph search algorithms such as Breadth-First Search (BFS) and Depth-First Search (DFS) are fundamental techniques for traversing or searching graph data structures.

## BFS (Breadth-First Search)

BFS explores all reachable vertices in layers. It uses a queue data structure to keep track of the nodes to be explored and a boolean array `visited[]` to keep track of visited vertices.

### Defining the Graph G for BFS:

```plaintext
Directed Graph G:
Vertices V = {1, 2, 3, 4, 5}
Edges E = {(2,1), (3,1), (2,3), (3,5), (4,2), (4,5)}
```

### BFS Algorithm Pseudocode:

```python
def BFS(G, S):
    queue = []
    queue.append(S)
    visited[S] = True

    while queue:
        u = queue.pop(0)  # dequeue the first element
        # Process u or perform some operations

        for v in G.neighbors(u):
            if not visited[v]:
                queue.append(v)
                visited[v] = True
```

#### For the example graph G, BFS might explore the vertices as:

```plaintext
Layers:
- Layer 0: 2
- Layer 1: 1, 3
- Layer 2: 4
- Layer 3: 5
```

### Time Complexity:

The time complexity of BFS is O(n + m), where n is the number of vertices and m is the number of edges.

## DFS (Depth-First Search)

DFS explores as far as possible along each branch before backtracking. It uses recursion and a boolean array `visited[]` to accomplish this.

### DFS Algorithm Pseudocode:

```python
def DFS(G, S, visited):
    visited[S] = True
    # Process S or perform some operations

    for v in G.neighbors(S):
        if not visited[v]:
            DFS(G, v, visited)
```

### Visiting All Vertices with DFS:

If some vertices are not connected, the time complexity is O(m).

```python
def DFS_All(G):
    visited = [False] * len(G.vertices)

    for S in range(len(G.vertices)):
        if not visited[S]:
            DFS(G, S, visited)
```

### Time Complexity:

The time complexity of DFS is O(n + m), where n is the number of vertices and m is the number of edges.

## DAG (Directed Acyclic Graph) and Topological Sort

DAGs do not have cycles, and a topological sort of a DAG lists all vertices in linear order, ensuring that for every directed edge u -> v, vertex u comes before v in the ordering.

### Topological Sort Example:

```plaintext
Directed Acyclic Graph:
Vertices V = {1, 2, 3, 4}
Edges E = {(2,3), (3,4), (2,4), (1,2)}
```

A topological sort might produce the sequence 1 -> 2 -> 3 -> 4.

---
