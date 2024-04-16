# Let's simulate the disjoint-set operations with path compression

# Initially, each element is in its own set
parent = {i: i for i in range(1, 9)}
rank = {i: 0 for i in range(1, 9)}


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # Path compression
    return parent[x]


def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        if rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        elif rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        else:
            parent[rootX] = rootY
            rank[rootY] += 1


# Perform the union operations as specified
union(1, 2)
union(3, 4)
union(5, 6)
union(7, 8)
union(1, 4)
union(6, 7)
union(4, 5)

# Perform the find operation
find_1 = find(1)

# The state of the disjoint-set
print('parent: ', parent, 'find_1: ', find_1)
