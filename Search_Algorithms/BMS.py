import pandas as pd
import numpy as np
import networkx as nx
from collections import deque

# Load CSV files
nodes_df = pd.read_csv('node_positions.csv')
G = nx.Graph()

# Add nodes to the graph
for index, row in nodes_df.iterrows():
    G.add_node(row['Node'], pos=(row['X'], row['Y']))

# Define edges
for i in range(len(nodes_df)):
    for j in range(i + 1, len(nodes_df)):
        node1 = nodes_df.iloc[i]['Node']
        node2 = nodes_df.iloc[j]['Node']
        distance = np.sqrt((nodes_df.iloc[j]['X'] - nodes_df.iloc[i]['X']) ** 2 + 
                           (nodes_df.iloc[j]['Y'] - nodes_df.iloc[i]['Y']) ** 2)
        G.add_edge(node1, node2, weight=distance)

def british_museum_search(graph, start_node, goal_node):
    visited = set()
    queue = deque([(start_node, [start_node], 0)]) 
    total_cost = 0
    output = []
    found_path = None

    while queue:
        current_node, path, current_cost = queue.popleft()
        if current_node not in visited:
            visited.add(current_node)

            if current_node == goal_node:  
                found_path = path
                total_cost = current_cost
                break

            for neighbor in graph.neighbors(current_node):
                edge_weight = graph[current_node][neighbor]['weight']
                new_cost = current_cost + edge_weight
                new_path = path + [neighbor]
                queue.append((neighbor, new_path, new_cost))
                output.append(f"||{current_node}||---{edge_weight:.2f}--->||{neighbor}||")

    if found_path:
        print("\n".join(output))
        print(f"Path to Goal Node ({goal_node}): {' -> '.join(map(str, found_path))}")
        print(f"Total Cost: {total_cost:.2f}")
    else:
        print(f"Goal Node ({goal_node}) not reached.")
    
    return visited

start_node = 1  # Replace with your actual start node as an integer
goal_node = 5   # Replace with your desired goal node as an integer
visited_nodes = british_museum_search(G, start_node, goal_node)
print("All visited nodes:", visited_nodes)
