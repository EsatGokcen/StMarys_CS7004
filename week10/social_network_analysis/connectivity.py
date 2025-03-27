import networkx as nx
import matplotlib.pyplot as plt

# Define the students (nodes) and their friendships (edges)
students = ['Aisha', 'Carlos', 'Mei', 'Arun', 'Billy', 'Jamil', 'Sofia', 'Raj', 'Priya', 'Omar', 'Emma', 'Diego']
friendships = [
    ('Aisha', 'Carlos'),
    ('Aisha', 'Arun'),
    ('Carlos', 'Mei'),
    ('Carlos', 'Billy'),
    ('Mei', 'Jamil'),
    ('Arun', 'Billy'),
    ('Fatima', 'Jamil'),
    ('Sofia', 'Raj'),
    ('Raj', 'Priya'),
    ('Priya', 'Omar'),
    ('Emma', 'Diego'),
    ('Diego', 'Jamil')
]

# Create an undirected graph
G = nx.Graph()

# Add nodes and edges to the graph
G.add_nodes_from(students)
G.add_edges_from(friendships)

# Check if the graph is connected
is_connected = nx.is_connected(G)

# Print the result
if is_connected:
    print("The social network is connected.")
else:
    print("The social network is not connected.")

# Find connected components
connected_components = list(nx.connected_components(G))

# Print the connected components
print("Connected Components (Clusters):")
for i, component in enumerate(connected_components, 1):
    print(f"Cluster {i}: {component}")

# Draw the graph
plt.figure(figsize=(12, 8))
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=12, font_color='black')
plt.title("Social Network of Friends")
plt.show()
