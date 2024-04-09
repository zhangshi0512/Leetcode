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

    # Print the table
    print("Iteration table showing shortest paths from S:")
    for i, distances in enumerate(table_bf):
        print(f"Iteration {i+1}: {distances}")

    # Print shortest path tree result for verification
    print("\nShortest path tree from node S:")
    for node, predecessor in predecessors_bf.items():
        if predecessor is not None:
            print(f"{predecessor} -> {node}")

except ValueError as e:
    print(e)
