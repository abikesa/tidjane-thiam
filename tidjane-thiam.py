import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import os

# Ensure the output directory exists
os.makedirs("images", exist_ok=True)

# Define the neural network fractal with updated labels
def define_layers():
    return {
        'Nonself': [
            'Household Wealth', 'Firm Records', 'Disclosure Risk', 
            'Other Governments', 'Accounts/Databases', 'Instruments/Contracts'
        ],
        'Self': ['Government'],  
        'Conflict': ['Nationalism', 'Faustian Bargain'],  
        'Negotiation': ['Emergence', 'Obfuscation', 'Derivatives'],  
        "Flourishing": ['Bluff', 'Scaling', 'Rituals', 'Variation', 'Culture']  
    }

# Maintain color assignments with corrected node labels
def assign_colors():
    color_map = {
        'yellow': ['Government'],  
        'paleturquoise': ['Instruments/Contracts', 'Faustian Bargain', 'Derivatives', 'Culture'],  
        'lightgreen': ['Accounts/Databases', 'Obfuscation', 'Scaling', 'Variation', 'Rituals'],  
        'lightsalmon': [
            'Disclosure Risk', 'Other Governments', 'Nationalism',  
            'Emergence', 'Bluff', 'Household Wealth', 'Firm Records'
        ],
    }
    return {node: color for color, nodes in color_map.items() for node in nodes}

# Calculate positions (top-down layout)
def calculate_positions(layer, y_offset):
    x_positions = np.linspace(-len(layer) / 2, len(layer) / 2, len(layer))
    return [(x, y_offset) for x in x_positions]

# Create and visualize the neural network graph (top-down orientation)
def visualize_nn():
    layers = define_layers()
    colors = assign_colors()
    G = nx.DiGraph()
    pos = {}
    node_colors = []

    # Add nodes and assign top-down positions
    for i, (layer_name, nodes) in enumerate(reversed(list(layers.items()))):
        positions = calculate_positions(nodes, y_offset=i * -2)
        for node, position in zip(nodes, positions):
            G.add_node(node, layer=layer_name)
            pos[node] = position
            node_colors.append(colors.get(node, 'lightgray'))

    # Add edges between consecutive layers
    layer_names = list(layers.keys())
    for i in range(len(layer_names) - 1):
        source_layer, target_layer = layer_names[i], layer_names[i + 1]
        for source in layers[source_layer]:
            for target in layers[target_layer]:
                G.add_edge(source, target)

    # Draw the graph
    plt.figure(figsize=(14, 10))
    nx.draw(
        G, pos, with_labels=True, node_color=node_colors, edge_color='gray',
        node_size=3000, font_size=13, connectionstyle="arc3,rad=0.2"
    )
    plt.title("Tidjane Thiam", fontsize=24)
    plt.savefig("images/tidgane-thiam.jpeg", dpi=300, bbox_inches='tight')

# Run the visualization
visualize_nn()
