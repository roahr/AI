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

def beam_search(graph, start_node, goal_node, beam_width):
    visited = set()
    queue = [(start_node, [start_node], 0)] 
    output = []
    total_cost = 0
    found_path = None

    print("============================ OPERATIONS PERFORMED ============================")
    while queue:

        queue.sort(key=lambda x: generate_heuristic(x[0], goal_node))
        
        queue = queue[:beam_width]
        
        new_queue = []
        for current_node, path, current_cost in queue:
            if current_node == goal_node:
                found_path = path
                total_cost = current_cost
                break
            
            if current_node not in visited:
                visited.add(current_node)
                
                for neighbor in graph.neighbors(current_node):
                    if neighbor not in visited:
                        edge_weight = graph[current_node][neighbor]['weight']
                        new_cost = current_cost + edge_weight
                        new_path = path + [neighbor]
                        new_queue.append((neighbor, new_path, new_cost))
                        output.append(f"Operation: ||{current_node}||---{edge_weight:.2f}--->||{neighbor}||")
        
        if found_path:
            break

        queue = new_queue  
    
    if found_path:
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
beam_width = 2  
visited_nodes = beam_search(G, start_node, goal_node, beam_width)
