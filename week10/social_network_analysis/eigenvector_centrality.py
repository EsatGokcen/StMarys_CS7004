import networkx as nx

# Create a new undirected graph
G = nx.Graph()

# Add nodes and edges
nodes = ('A', 'B', 'C', 'D')
edges = (('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'))
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Calculate eigenvector centrality
eigenvector_centrality = nx.eigenvector_centrality(G)

# Print the eigenvector centrality of each node
for node, centrality in eigenvector_centrality.items():
    print(f"Node {node} has eigenvector centrality: {centrality:.2f}")