from flask import Flask, render_template, request, send_file
import networkx as nx
import matplotlib.pyplot as plt
import random
import math
import io
import csv

app = Flask(__name__)

# Global variables to store the tree and positions
global_tree = None
global_positions = None

def generate_random_tree(num_nodes):
    tree = nx.DiGraph()  
    positions = {}
    
    positions[1] = (random.uniform(0, 10), random.uniform(0, 10))
    tree.add_node(1, pos=positions[1])

    for node in range(2, num_nodes + 1):
        while True:
            new_position = (random.uniform(0, 10), random.uniform(0, 10))
            if all(euclidean_distance(new_position, positions[existing_node]) >= 3 for existing_node in positions): # Constraint to have space between nodes
                positions[node] = new_position
                tree.add_node(node, pos=new_position)
                break

        parent = random.randint(1, node - 1)  
        distance = euclidean_distance(positions[parent], positions[node])
        tree.add_edge(parent, node, weight=round(distance, 2))

    return tree, positions

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def visualize_tree(tree, positions, start_node, goal_node):
    fig, ax = plt.subplots(figsize=(6, 6))
    
    node_colors = ['red' if node == start_node else 'green' if node == goal_node else 'lightblue' for node in tree.nodes()]
    nx.draw(tree, positions, with_labels=True, node_color=node_colors, node_size=2000, font_size=10, font_weight='bold', ax=ax)
    edge_labels = nx.get_edge_attributes(tree, 'weight')
    nx.draw_networkx_edge_labels(tree, positions, edge_labels=edge_labels, font_color='red', ax=ax)

    output = io.BytesIO()
    plt.savefig(output, format='png')
    plt.close(fig)
    output.seek(0)
    return output

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_tree', methods=['POST'])
def generate_tree():
    global global_tree, global_positions  # Use global variables
    num_nodes = int(request.form['num_nodes'])
    start_node = int(request.form['start_node'])
    goal_node = int(request.form['goal_node'])

    # Generate the tree and store it in global variables
    global_tree, global_positions = generate_random_tree(num_nodes)

    img = visualize_tree(global_tree, global_positions, start_node, goal_node)
    return send_file(img, mimetype='image/png')

@app.route('/download_positions_csv', methods=['POST'])
def download_positions_csv():
    global global_positions  # Use global variable

    output_positions = io.StringIO()
    writer_positions = csv.writer(output_positions)

    writer_positions.writerow(["Node", "X", "Y"])
    for node, pos in global_positions.items():
        writer_positions.writerow([node, pos[0], pos[1]])

    output_positions.seek(0)

    return send_file(
        io.BytesIO(output_positions.getvalue().encode('utf-8')),
        mimetype='text/csv',
        as_attachment=True,
        download_name='node_positions.csv'
    )

@app.route('/download_path_details_csv', methods=['POST'])
def download_path_details_csv():
    global global_tree  # Use global variable

    # Prepare to write edge details
    output_edges = io.StringIO()
    writer_edges = csv.writer(output_edges)

    writer_edges.writerow(["Source Node", "Target Node", "Weight"])
    for u, v, data in global_tree.edges(data=True):
        writer_edges.writerow([u, v, data['weight']])

    output_edges.seek(0)

    return send_file(
        io.BytesIO(output_edges.getvalue().encode('utf-8')),
        mimetype='text/csv',
        as_attachment=True,
        download_name='path_details.csv'
    )

if __name__ == '__main__':
    app.run(debug=True)
