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

---

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

## Graph Algorithms: Topological Sort and Connected Components

### Topological Sort using BFS (Kahn's Algorithm)

Assuming we have an in-degree array to keep track of the number of edges coming into each vertex, we can perform topological sorting with the following algorithm:

```python
# Step 1: Calculate in-degrees of all vertices
in_degree = [0] * n
for u in range(n):
    for v in G.neighbors(u):
        in_degree[v] += 1

# Step 2: Enqueue vertices with in-degree 0 (starting points)
queue = []
for u in range(n):
    if in_degree[u] == 0:
        queue.append(u)

# Step 3: Process vertices with in-degree 0 and update in-degrees
while queue:
    u = queue.pop(0)
    for v in G.neighbors(u):
        in_degree[v] -= 1
        if in_degree[v] == 0:
            queue.append(v)
```

The overall running time of this algorithm is `O(n + m)`.

### Depth-First Search (DFS) for Topological Sorting

Here is how we can modify the DFS algorithm to perform a topological sort:

```python
def DFS(G, s, visited, L):
    visited[s] = True
    for u in G.neighbors(s):
        if not visited[u]:
            DFS(G, u, visited, L)
    L.append(s)

def DFS_All(G):
    visited = [False] * len(G.vertices)
    L = []
    for s in range(len(G.vertices)):
        if not visited[s]:
            DFS(G, s, visited, L)
    L.reverse()
    return L
```

The modified DFS algorithm with a list `L` stores the vertices in a way that can be reversed at the end to provide a topological ordering. The time complexity of this approach is `O(n + m)`.

### Finding Connected Components in an Undirected Graph

To find connected components, we can use a breadth-first search starting from each unvisited vertex:

```python
def BFS_All(G):
    visited = [False] * len(G.vertices)
    CC = [None] * len(G.vertices)  # Connected Components
    id = 0  # Component ID

    for s in range(len(G.vertices)):
        if not visited[s]:
            id += 1
            BFS(G, s, visited, CC, id)
    return CC, id

def BFS(G, s, visited, CC, id):
    visited[s] = True
    queue = [s]
    while queue:
        u = queue.pop(0)
        CC[u] = id
        for v in G.neighbors(u):
            if not visited[v]:
                queue.append(v)
                visited[v] = True
```

The time complexity for finding connected components is `O(n + m)`.

### Representing a Grid for Land and Water Mapping

Consider a grid where 0 represents water and 1 represents land. We can traverse this grid to identify distinct land areas or 'islands'.

| 0   | 1   | 1   | 0   | 1   |
| --- | --- | --- | --- | --- |
| 0   | 1   | 0   | 0   | 0   |
| 1   | 0   | 0   | 1   | 1   |
| 0   | 0   | 0   | 1   | 1   |
| 0   | 0   | 1   | 1   | 1   |

---

## Graph Theory: Cycle Detection, DFS, and SCC

### Directed Acyclic Graph (DAG) and Cycle Detection

A Directed Acyclic Graph, or DAG, is a directed graph with no directed cycles. To detect cycles in a DAG, we can use the following method:

```plaintext
To identify a cycle:
1. Identify the vertices with 0 in-degree, remove them.
2. Keep doing so until you cannot remove anymore or the graph has been completely removed.
3. If the graph cannot be completely removed, there's a cycle.
```

For example, given two graphs G1 and G2:

- `G1`: Contains a cycle among the vertices.
- `G2`: No cycle, as all vertices are removed by iteratively removing those with 0 in-degree.

### Depth-First Search (DFS) for Cycle Detection

DFS is a fundamental algorithm in graph theory that can be used for various purposes, including cycle detection:

```C
DFS(G, u, color[]) {
    color[u] = Grey; // Mark the vertex as being visited
    for(v in G.neighbors(u)) {
        if (color[v] == White) {
            if (DFS(G, v, color)) return True; // Found a cycle
        } else if (color[v] == Grey) {
            return True; // Found a cycle
        }
    }
    color[u] = Black; // Mark the vertex as finished
    return False;
}
```

### Strongly Connected Components (SCC)

In a directed graph, a Strongly Connected Component (SCC) is a subset of the graph where every vertex is reachable from every other vertex in the subset.

```plaintext
u, v ∈ SCC if and only if there exists a path from u to v and v to u.
```

### Graph Representation in Plaintext

For a directed graph `G`, a plaintext representation can be as follows:

- `Directed Graph G`: {(a->b), (b->c), ..., (g->h)}

For strongly connected components:

- `G1`: Represents a graph with one SCC.
- `G2`: Represents a graph with separate SCCs.

---
