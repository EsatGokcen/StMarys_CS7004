import networkx as nx

# Create a new undirected graph
G = nx.Graph()

# Add nodes and edges
nodes = ('A', 'B', 'C', 'D')
edges = (('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'))
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Calculate degree centrality
degree_centrality = nx.degree_centrality(G)

# Print the degree centrality of each node
for node, centrality in degree_centrality.items():
    print(f"Node {node} has degree centrality: {centrality:.2f}")