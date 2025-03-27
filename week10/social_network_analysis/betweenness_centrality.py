import networkx as nx

# Create a new undirected graph
G = nx.Graph()

# Add nodes and edges
nodes = ('A', 'B', 'C', 'D')
edges = (('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'))
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Calculate betweenness centrality
betweenness_centrality = nx.betweenness_centrality(G)

# Print the betweenness centrality of each node
for node, centrality in betweenness_centrality.items():
    print(f"Node {node} has betweenness centrality: {centrality:.2f}")