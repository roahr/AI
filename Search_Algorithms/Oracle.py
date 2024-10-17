import pandas as pd
import networkx as nx
import math

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

def oracle_search(graph, start_node, goal_node):
    visited = set()
    current_node = start_node
    total_cost = 0
    path = [start_node]
    output = []

    print("============================ OPERATIONS PERFORMED ============================")
    while current_node != goal_node:
        visited.add(current_node)

        neighbors = [(neighbor, graph[current_node][neighbor]['weight']) for neighbor in graph.neighbors(current_node)]
        if not neighbors:
            break
        
        best_neighbor = min(neighbors, key=lambda x: generate_heuristic(x[0], goal_node) + x[1])
        best_weight = best_neighbor[1]
        
        path.append(best_neighbor[0])
        total_cost += best_weight
        output.append(f"Operation: ||{current_node}||---{best_weight:.2f}--->||{best_neighbor[0]}||")
        
        current_node = best_neighbor[0]

    if current_node == goal_node:
        print("\n".join(output))
        print("====================================================================================")
        print(f"\nPath Found: {' -> '.join(map(str, path))}")
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
visited_nodes = oracle_search(G, start_node, goal_node)
