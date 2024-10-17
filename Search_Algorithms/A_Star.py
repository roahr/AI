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

def a_star_search(graph, start_node, goal_node):
    visited = set()
    min_heap = []
    heapq.heappush(min_heap, (0, start_node, [start_node], 0))  
    total_cost = float('inf')
    output = []

    print("============================ OPERATIONS PERFORMED ============================")

    while min_heap:
        f_score, current_node, path, g_score = heapq.heappop(min_heap)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal_node:
            total_cost = g_score
            found_path = path
            break

        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                edge_weight = graph[current_node][neighbor]['weight']
                new_g_score = g_score + edge_weight
                heuristic = generate_heuristic(neighbor, goal_node)
                new_f_score = new_g_score + heuristic
                
                heapq.heappush(min_heap, (new_f_score, neighbor, path + [neighbor], new_g_score))
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
visited_nodes = a_star_search(G, start_node, goal_node)
