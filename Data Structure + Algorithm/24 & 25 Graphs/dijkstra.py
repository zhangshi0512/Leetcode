# Define the graph from the image as a dictionary. The keys are the nodes, and the values are dictionaries
# of the neighbors with the edge weights.
graph = {
    'A': {'B': 1, 'E': 4},
    'B': {'A': 1, 'C': 2, 'F': 8},
    'C': {'B': 2, 'D': 1, 'F': 6, 'G': 2},
    'D': {'C': 1, 'H': 4},
    'E': {'A': 4, 'F': 5},
    'F': {'B': 8, 'C': 6, 'E': 5, 'G': 1},
    'G': {'C': 2, 'F': 1, 'H': 1},
    'H': {'G': 1, 'D': 4}
}


def dijkstra(graph, start):
    # Initialization
    unvisited_nodes = list(graph.keys())
    shortest_path = {node: (float('inf'), None) for node in unvisited_nodes}
    shortest_path[start] = (0, start)
    current_node = start

    # Table to visualize the progress
    table = []

    while unvisited_nodes:
        # Update the distances to the neighboring nodes
        for neighbor, distance in graph[current_node].items():
            new_distance = shortest_path[current_node][0] + distance
            if new_distance < shortest_path[neighbor][0]:
                shortest_path[neighbor] = (new_distance, current_node)

        # Mark the current node as visited
        unvisited_nodes.remove(current_node)

        # Add current distances to the table for visualization
        table.append([shortest_path[node][0] for node in graph.keys()])

        # Find the next node with the smallest distance
        current_node = None
        current_smallest_distance = float('inf')
        for node in unvisited_nodes:
            if shortest_path[node][0] < current_smallest_distance:
                current_smallest_distance = shortest_path[node][0]
                current_node = node

        # If all remaining nodes are unreachable, break
        if current_node is None:
            break

    return shortest_path, table


# Run the Dijkstra's algorithm
shortest_paths, table = dijkstra(graph, 'A')

# Print the table
print("Iteration table showing shortest paths from A:")
print(f"{'Node':<10} {'Iter1':<10} {'Iter2':<10} {'Iter3':<10} {'Iter4':<10} {'Iter5':<10} {'Iter6':<10} {'Iter7':<10} {'Iter8':<10}")
for i, node in enumerate(graph.keys()):
    distances = [row[i] if row[i] != float('inf') else '∞' for row in table]
    print(f"{node:<10} {' '.join(f'{dist:<10}' for dist in distances)}")

# Print shortest path result for verification
print("\nShortest path from node A to other nodes:")
for node, (dist, prev) in shortest_paths.items():
    print(f"A to {node}: {dist} via {prev}")
