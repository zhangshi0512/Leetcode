import heapq
import itertools

# Graph representation as an adjacency list
graph = {
    'A': {'B': 1, 'E': 4},
    'B': {'A': 1, 'C': 2, 'F': 6, 'E': 8},
    'C': {'B': 2, 'D': 3, 'G': 6, 'F': 6},
    'D': {'C': 3, 'H': 4},
    'E': {'A': 4, 'B': 8, 'F': 5},
    'F': {'B': 6, 'C': 6, 'E': 5, 'G': 1},
    'G': {'C': 6, 'F': 1, 'H': 1},
    'H': {'G': 1, 'D': 4}
}

# Prim's algorithm


def prims(graph, starting_vertex):
    mst = []
    visited = set([starting_vertex])
    edges = [
        (cost, starting_vertex, to)
        for to, cost in graph[starting_vertex].items()
    ]
    heapq.heapify(edges)

    # Table to record the intermediate values of the cost array
    cost_table = []

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, cost))

            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost, to, to_next))

    # Record the current edge weights
    if edges:  # Check if there are any edges left to process
        cost_table.append({
            vertex: min((edge[0] for edge in edges if edge[1]
                        == vertex), default=float('inf'))
            for vertex in graph.keys()
            if vertex not in visited
        })

    return mst, cost_table


# Run Prim's algorithm starting from node A
mst_prims, cost_table_prims = prims(graph, 'A')


# Kruskal's algorithm
def make_set(v):
    parent[v] = v
    rank[v] = 0


def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


def union(v1, v2):
    root1 = find(v1)
    root2 = find(v2)
    if root1 != root2:
        if rank[root1] < rank[root2]:
            parent[root1] = root2
        else:
            parent[root2] = root1
            if rank[root1] == rank[root2]:
                rank[root1] += 1


def kruskal(graph):
    for v in graph:
        make_set(v)

    mst = []
    edges = sorted([(cost, v1, v2) for v1, adj in graph.items()
                   for v2, cost in adj.items()], key=lambda e: e[0])

    disjoint_set_snapshots = []  # to record the state of the disjoint set structure
    for edge in edges:
        cost, v1, v2 = edge
        if find(v1) != find(v2):
            union(v1, v2)
            mst.append(edge)
            # Record a snapshot of the disjoint-set structure
            disjoint_set_snapshots.append((edge, dict(parent), dict(rank)))

    return mst, disjoint_set_snapshots


parent = dict()
rank = dict()

# Run Kruskal's algorithm
mst_kruskal, disjoint_set_snapshots = kruskal(graph)

print('mst_prims:', mst_prims, 'cost_table_prims:', cost_table_prims)

print('mst_kruskal:', mst_kruskal,
      'disjoint_set_snapshots:', disjoint_set_snapshots)
