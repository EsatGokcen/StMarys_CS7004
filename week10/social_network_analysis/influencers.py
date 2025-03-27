import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add nodes
nodes = ["Ananya", "Raj", "Yuki", "Kai", "Aisha", "Luca"]
G.add_nodes_from(nodes)

# Add edges
edges = [("Ananya", "Raj"), ("Ananya", "Yuki"), ("Raj", "Yuki"), ("Yuki", "Ananya"), ("Yuki", "Kai"),
         ("Kai", "Aisha"), ("Aisha", "Luca"), ("Luca", "Raj"), ("Luca", "Ananya")]
G.add_edges_from(edges)

# Compute the layout for the nodes
pos = nx.spring_layout(G, seed=42)  # seed for reproducibility

# Create a matplotlib figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Draw nodes
nx.draw_networkx_nodes(G, pos, ax=ax, node_color='lightblue', node_size=2000)

# Draw edges
nx.draw_networkx_edges(G, pos, ax=ax, edge_color='gray')

# Draw labels
nx.draw_networkx_labels(G, pos, ax=ax, font_size=16, font_weight='bold')

# Set title and display the plot
plt.title("Directed Graph")
plt.show()