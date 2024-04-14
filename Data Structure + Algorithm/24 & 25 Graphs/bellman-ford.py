# Define the graph from the image as a dictionary of dictionaries, with outer keys as source nodes
# and inner keys as destination nodes, along with the edge weights.
graph_bf = {
    'S': {'A': 7, 'C': 6, 'E': 6, 'F': 5},
    'A': {'C': -2, 'B': 4},
    'B': {'H': -4, 'G': -2},
    'C': {'D': 2, 'F': 1},
    'D': {},
    'E': {'H': 3, 'F': -2},
    'F': {'D': 3},
    'G': {'I': -1},
    'H': {'G': 1},
    'I': {'H': 1}
}

# Bellman-Ford algorithm implementation


def bellman_ford(graph, source):
    # Step 1: Initialize distances from source to all other nodes as infinity and 0 for source itself
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    predecessors = {node: None for node in graph}

    # Table to visualize the progress after each iteration
    table = [distances.copy()]

    # Step 2: Relaxation, repeat V-1 times
    for _ in range(len(graph) - 1):
        for u in graph:
            for v in graph[u]:
                # Relaxation step
                if distances[u] + graph[u][v] < distances[v]:
                    distances[v] = distances[u] + graph[u][v]
                    predecessors[v] = u
        table.append(distances.copy())

    # Step 3: Check for negative weight cycles
    for u in graph:
        for v in graph[u]:
            if distances[u] + graph[u][v] < distances[v]:
                raise ValueError("Graph contains a negative weight cycle")

    return distances, table, predecessors


# Start Bellman-Ford algorithm from node S
try:
    shortest_paths_bf, table_bf, predecessors_bf = bellman_ford(graph_bf, 'S')

    # Extracting nodes for table headers
    vertices = list(graph_bf.keys())

    # Print the table
    print("Iteration table showing shortest paths from S:")
    print(f"{'Node':<10}", end='')
    # Assuming vertices is the list/set of all nodes in the graph
    for i in range(len(vertices)):
        print(f"{'Iter'+str(i+1):<10}", end='')
    print()

    for node in vertices:
        print(f"{node:<10}", end='')
        for i in range(len(vertices)):
            dist = table_bf[i].get(node, float('inf'))
            if dist == float('inf'):
                print(f"{'∞':<10}", end='')
            else:
                print(f"{dist:<10}", end='')
        print()

    print("\nShortest path from node S to other nodes:")
    for node, dist in shortest_paths_bf.items():
        print(f"S to {node}: {dist}")


except ValueError as e:
    print(e)


shortest_paths = {
    'S': 0,
    'A': 7,
    'B': 11,
    'C': 5,
    'D': 7,
    'E': 6,
    'F': 4,
    'G': 8,
    'H': 7,
    'I': 7
}

# This would need logic based on how parent nodes were determined
# during your path calculations:
parent_nodes = {
    'S': None,  # Source has no parent
    'A': 'S',
    'B': 'D',
    'C': 'F',
    'D': 'E',
    'E': 'F',
    'F': 'S',
    'G': 'F',
    'H': 'I',
    'I': 'H'
}


def construct_shortest_path_tree(parent_nodes):
    tree = {}
    for node in parent_nodes:
        parent = parent_nodes[node]
        if parent:
            if parent not in tree:
                tree[parent] = [node]
            else:
                tree[parent].append(node)
    return tree


tree = construct_shortest_path_tree(parent_nodes)
print(tree)
