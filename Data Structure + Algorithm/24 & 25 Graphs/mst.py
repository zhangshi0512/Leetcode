# There was an error in the previous implementation of the Kruskal's algorithm. Let's try a simpler approach.

# Define the graph using an adjacency list with edge weights
edges = [
    ('A', 'E', 1), ('A', 'B', 6), ('E', 'F', 1), ('E', 'B', 2), ('B', 'F', 2),
    ('B', 'C', 5), ('F', 'C', 5), ('F', 'G', 3), ('C', 'G', 4), ('C', 'D', 6),
    ('G', 'D', 5), ('G', 'H', 3), ('D', 'H', 7)
]

# Initialize disjoint sets
parent = {u: u for u, v, w in edges}
rank = {u: 0 for u, v, w in edges}
for u, v, w in edges:
    parent[v] = v
    rank[v] = 0

# Function to find the set representative


def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])
    return parent[u]

# Function to union two sets


def union(u, v):
    u = find(u)
    v = find(v)
    if u != v:
        if rank[u] < rank[v]:
            parent[u] = v
        elif rank[u] > rank[v]:
            parent[v] = u
        else:
            parent[u] = v
            rank[v] += 1
        return True
    return False

# Kruskal's algorithm to find the minimum spanning tree


def kruskal(edges):
    mst = []
    cost = 0
    for u, v, w in sorted(edges, key=lambda x: x[2]):
        if union(u, v):
            mst.append((u, v, w))
            cost += w
    return mst, cost


# Find the MST and its cost
mst, cost = kruskal(edges)

# To determine the number of minimum spanning trees, we can check for edges in the MST with the same weight
# that could lead to multiple equivalent minimum spanning trees.
# However, in a graph with unique edge weights, Kruskal's algorithm will always produce a unique MST.

# Check for edges with the same weight
same_weight_edges = {}
for u, v, w in edges:
    if w not in same_weight_edges:
        same_weight_edges[w] = []
    same_weight_edges[w].append((u, v))

# Count how many MSTs are possible considering edges with the same weight
mst_count = 1
for w, edge_list in same_weight_edges.items():
    if len(edge_list) > 1:
        # If there are multiple edges with the same weight, they could potentially form different MSTs
        mst_count *= len(edge_list)

print('cost: ', cost, 'mst count: ', mst_count, 'mst: ', mst)
