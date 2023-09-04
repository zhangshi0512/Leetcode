"""
Consider a n undirected graph where each
edge weighs 6 units. Each of the nodes is
labeled consecutively fro m 1 to n.

You will be given a number Of queries. For
each query, yo u will be given a list 0f
edges describing a n undirected graph.
After you create a representation Of the
graph, you must determine and report
the shortest distance tO each Of the other
nodes from a given starting position using
the breadth-first search algorithm (BFS).
Return a n array Of distances from the
start node in node number order. If a
node is unreachable, return - 1 for that
node.

Function Description
Complete the bfs function in the editor
below. If a node is unreachable, i ts
distance is - 1.
bfs has the following parameter(s):
· int n: the number Of nodes
· int m: the number Of edges
· int edges[m][2] start and end nodes for edges
· int s: the node tO sta rt traversals from
Returns
int[n-1]: the distances tO nodes in
increasing node number order, not
including the start node (-1 if a node is not
reachable)

Input Format
The fi rst line contains a n integer q, the
number Of queries. Each Of the following
q sets 0f lines has the following format:

- The first line contains two space-
separated integers and m, the
number Of nodes and edges in the
graph.
- Each line Of the m subsequent lines
contains tWO space-separated integers,
u and v that describe a n edge between
nodes u and v.
- The last line contains a single integer, S,
the node number to start from.

Sample Input:
4 2
1 2
1 3
3 1
2 3

Sample Output
6 6 -1
-1 6
"""

# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
# 1. INTEGER n
# 2. INTEGER m
# 3. 2D_INTEGER_ARRAY edges
# 4. INTEGER S
from collections import defaultdict, deque


def bfs(n, m, edges, s):
    # Create an adjacency list representation of the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Initialize distances and visited arrays
    distances = [-1] * (n + 1)  # Using 1-based indexing
    visited = [False] * (n + 1)

    # BFS
    queue = deque([s])
    distances[s] = 0
    visited[s] = True

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                distances[neighbor] = distances[node] + 6

    # Prepare the final output, excluding the starting node
    result = [distances[i] for i in range(1, n + 1) if i != s]
    return result


# Test the function with the provided sample
sample_input = [
    (4, 2, [(1, 2), (1, 3)], 1),
    (3, 1, [(2, 3)], 3)
]
outputs = [bfs(*inp) for inp in sample_input]
print(outputs)
