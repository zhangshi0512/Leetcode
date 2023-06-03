# Big O Analysis

Here is a table with the Big O time and space complexity for common operations on a Graph:

| Operation                  | Time Complexity | Space Complexity |
| -------------------------- | --------------- | ---------------- |
| Add Vertex                 | O(1)            | O(V)             |
| Add Edge                   | O(1)            | O(E)             |
| Remove Vertex              | O(V + E)        | O(V + E)         |
| Remove Edge                | O(E)            | O(E)             |
| Query                      | O(1)            | O(V)             |
| BFS (Breadth First Search) | O(V + E)        | O(V)             |
| DFS (Depth First Search)   | O(V + E)        | O(V)             |

Note: The complexities mentioned are for an adjacency list representation of the graph. The time complexity may change if a different data structure (like adjacency matrix) is used for the representation. Here V represents the number of vertices and E represents the number of edges.

# Code Template

Now, let's implement a simple undirected graph in Python:

```python
class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].remove(vertex2)
            self.graph[vertex2].remove(vertex1)

    def remove_vertex(self, vertex):
        while self.graph[vertex]:
            self.remove_edge(vertex, self.graph[vertex][0])
        del self.graph[vertex]

    def bfs(self, vertex):
        visited = {vertex}
        queue = [vertex]
        while queue:
            vertex = queue.pop(0)
            print(vertex, end=' ')
            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        print()

    def dfs(self, vertex, visited=None):
        if visited is None:
            visited = set()
        visited.add(vertex)
        print(vertex, end=' ')
        for neighbour in self.graph[vertex]:
            if neighbour not in visited:
                self.dfs(neighbour, visited)
        return visited


# Sample usage:
g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_edge('A', 'B')
g.bfs('A')  # Output: A B
g.dfs('A')  # Output: A B
```

This graph implementation includes methods for adding and removing vertices and edges, and for performing Breadth-First Search (BFS) and Depth-First Search (DFS). Please note that this is a very basic implementation and doesn't include some features that you might need in a more advanced graph structure, such as handling of weighted edges or directed edges.
