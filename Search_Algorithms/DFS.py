import pandas as pd
import networkx as nx

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

def depth_first_search(graph, start_node, goal_node):
    visited = set()
    stack = [(start_node, [start_node], 0)]  
    total_cost = 0
    output = []
    found_path = None

    print("============================ OPERATIONS PERFORMED ============================")
    while stack:
        current_node, path, current_cost = stack.pop()
        if current_node not in visited:
            visited.add(current_node)

            if current_node == goal_node:  
                found_path = path
                total_cost = current_cost
                break

            for neighbor in graph.neighbors(current_node):
                if neighbor not in visited:  # Only consider unvisited neighbors
                    edge_weight = graph[current_node][neighbor]['weight']
                    new_cost = current_cost + edge_weight
                    new_path = path + [neighbor]
                    stack.append((neighbor, new_path, new_cost))
                    output.append(f"Operation: ||{current_node}||---{edge_weight:.2f}--->||{neighbor}||")

    
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
visited_nodes = depth_first_search(G, start_node, goal_node)
