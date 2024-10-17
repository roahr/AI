import pandas as pd
import networkx as nx
import math
import heapq

# Load node positions and path details
nodes_df = pd.read_csv('node_positions.csv')
paths_df = pd.read_csv('path_details.csv')
G = nx.DiGraph()  # Directed graph for AO*

# Add nodes to the graph
for index, row in nodes_df.iterrows():
    G.add_node(row['Node'], pos=(row['X'], row['Y']))

# Define edges
for index, row in paths_df.iterrows():
    G.add_edge(row['Source Node'], row['Target Node'], weight=row['Weight'])

# Heuristic generation (Euclidean distance)
def generate_heuristic(node, goal):
    node_pos = G.nodes[node]['pos']
    goal_pos = G.nodes[goal]['pos']
    return math.sqrt((node_pos[0] - goal_pos[0]) ** 2 + (node_pos[1] - goal_pos[1]) ** 2)

def ao_star_search(graph, start_node, goal_node):
    visited = set()
    costs = {start_node: 0}
    output = []
    queue = [(0, start_node)]  

    print("============================ OPERATIONS PERFORMED ============================")

    while queue:
        current_cost, current_node = heapq.heappop(queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor in graph.neighbors(current_node):
            edge_weight = graph[current_node][neighbor]['weight']
            new_cost = current_cost + edge_weight
            
            if neighbor not in visited:
                if neighbor not in costs or new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost
                    heapq.heappush(queue, (new_cost + generate_heuristic(neighbor, goal_node), neighbor))
                    output.append(f"Operation: ||{current_node}||---{edge_weight:.2f}--->||{neighbor}||")
                    
                    if neighbor == goal_node:
                        print("\n".join(output))
                        print("====================================================================================")
                        print(f"\nPath Found: {' -> '.join(map(str, visited))} -> {goal_node}")
                        print("====================================================================================")
                        print(f"Total Cost: {new_cost:.2f}")
                        print("====================================================================================")
                        return visited

    print(f"Goal Node ({goal_node}) not reached.")
    print("====================================================================================")
    
    visited_formatted = [int(node) for node in visited]
    print(f"All Visited Nodes: {visited_formatted}")
    print("====================================================================================")
    return visited_formatted

start_node = 1  # Source
goal_node = 5   # Goal
visited_nodes = ao_star_search(G, start_node, goal_node)
