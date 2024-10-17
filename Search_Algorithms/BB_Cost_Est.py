import pandas as pd
import networkx as nx
import math
import heapq

# Load node positions and path details
nodes_df = pd.read_csv('node_positions.csv')
paths_df = pd.read_csv('path_details.csv')
G = nx.Graph()

# Add nodes to the graph
for index, row in nodes_df.iterrows():
    G.add_node(row['Node'], pos=(row['X'], row['Y']))

# Define edges (bidirectional)
for index, row in paths_df.iterrows():
    G.add_edge(row['Source Node'], row['Target Node'], weight=row['Weight'])
    G.add_edge(row['Target Node'], row['Source Node'], weight=row['Weight'])  

# Heuristic generation (Euclidean distan)
def generate_heuristic(node, goal):
    node_pos = G.nodes[node]['pos']
    goal_pos = G.nodes[goal]['pos']
    return math.sqrt((node_pos[0] - goal_pos[0]) ** 2 + (node_pos[1] - goal_pos[1]) ** 2)

def branch_and_bound_cost_estimate(graph, start_node, goal_node):
    visited = set()
    min_heap = []
    heapq.heappush(min_heap, (0, start_node, [start_node], 0)) 
    total_cost = float('inf')
    output = []

    print("============================ OPERATIONS PERFORMED ============================")

    while min_heap:
        current_cost, current_node, path, current_total_cost = heapq.heappop(min_heap)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal_node:
            if current_total_cost < total_cost:
                total_cost = current_total_cost
                found_path = path
            continue

        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                edge_weight = graph[current_node][neighbor]['weight']
                new_total_cost = current_total_cost + edge_weight
                heuristic = generate_heuristic(neighbor, goal_node)
                heapq.heappush(min_heap, (new_total_cost + heuristic, neighbor, path + [neighbor], new_total_cost))
                output.append(f"Operation: ||{current_node}||---{edge_weight:.2f}--->||{neighbor}||")

    if total_cost < float('inf'):
        print("\n".join(output))
        print("====================================================================================")
        print(f"\nPath Found: {' -> '.join(map(str, found_path))}")
        print("====================================================================================")
        print(f"Total Cost: {total_cost:.2f}")
        print("====================================================================================")
    else:
        print(f"Goal Node ({goal_node}) not reached.")
        print("====================================================================================")

    visited_formatted = [int(node) for node in visited]
    print(f"All Visited Nodes: {visited_formatted}")
    print("====================================================================================")
    return visited_formatted

start_node = 1  # Source
goal_node = 5   # Goal
visited_nodes = branch_and_bound_cost_estimate(G, start_node, goal_node)
