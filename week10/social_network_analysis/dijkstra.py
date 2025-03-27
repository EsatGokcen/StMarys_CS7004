import networkx as nx
import matplotlib.pyplot as plt

# Create a new weighted graph
G = nx.Graph()

# Add nodes and edges with distances (weights)
edges = [
    ("A", "B", 10),
    ("A", "C", 15),
    ("B", "C", 12),
    ("B", "D", 15),
    ("C", "D", 10),
    ("C", "E", 5),
    ("D", "E", 8),
    ("D", "F", 20),
    ("E", "F", 10)
]

G.add_weighted_edges_from(edges)

# Find the shortest path from 'A' to 'F' using Dijkstra's algorithm
shortest_path = nx.shortest_path(G, source="A", target="F", weight='weight')
shortest_path_length = nx.shortest_path_length(G, source="A", target="F", weight='weight')

# Print the shortest path and its length
print(f"Shortest path from City A to City F: {shortest_path}")
print(f"Length of the path: {shortest_path_length} km")

# Draw the graph
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)  # Position nodes using the spring layout

# Draw the entire graph with weights
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, edge_color='gray', font_size=12, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f'{d["weight"]} km' for u, v, d in G.edges(data=True)})

# Highlight the shortest path
path_edges = list(zip(shortest_path, shortest_path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

# Show the plot
plt.title("Road Trip: Shortest Path from City A to City F")
plt.show()