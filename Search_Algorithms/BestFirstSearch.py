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

# Heuristic generation (Euclidean distance)
def generate_heuristic(node, goal):
    node_pos = G.nodes[node]['pos']
    goal_pos = G.nodes[goal]['pos']
    return math.sqrt((node_pos[0] - goal_pos[0]) ** 2 + (node_pos[1] - goal_pos[1]) ** 2)

def best_first_search(graph, start_node, goal_node):
    visited = set()
    min_heap = []
    heapq.heappush(min_heap, (generate_heuristic(start_node, goal_node), start_node, [start_node]))  
    output = []

    print("============================ OPERATIONS PERFORMED ============================")

    while min_heap:
        heuristic_value, current_node, path = heapq.heappop(min_heap)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal_node:
            print("\n".join(output))
            print("====================================================================================")
            print(f"\nPath Found: {' -> '.join(map(str, path))}")
            print("====================================================================================")
            print(f"Total Cost: {sum(graph[path[i]][path[i+1]]['weight'] for i in range(len(path) - 1)):.2f}")
            print("====================================================================================")
            return visited

        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                edge_weight = graph[current_node][neighbor]['weight']
                new_path = path + [neighbor]
                heapq.heappush(min_heap, (generate_heuristic(neighbor, goal_node), neighbor, new_path))
                output.append(f"Operation: ||{current_node}||---{edge_weight:.2f}--->||{neighbor}||")

    print(f"Goal Node ({goal_node}) not reached.")
    print("====================================================================================")
    
    visited_formatted = [int(node) for node in visited]
    print(f"All Visited Nodes: {visited_formatted}")
    print("====================================================================================")
    return visited_formatted

start_node = 1  # Source
goal_node = 5   # Goal
visited_nodes = best_first_search(G, start_node, goal_node)
