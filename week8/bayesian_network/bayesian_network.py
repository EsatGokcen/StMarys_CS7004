from week8.bayesian_network.node import Node

class BayesianNetwork:

    def __init__(self):
        self.__nodes = {}

    @property
    def get_nodes(self) -> dict[Node]:
        return self.__nodes

    def add_node(self, node: Node) -> None:
        self.__nodes.update({node.get_name(), node})

    def remove_node(self, node_name: str) -> None:
        del self.__nodes[node_name]

    def add_edge(self, parent_node: Node, child_node: Node) -> None:
        child_node.add_parent(parent_node)

    def remove_edge(self, parent_node: Node, child_node: Node) -> None:
        child_node.remove_parent(parent_node)