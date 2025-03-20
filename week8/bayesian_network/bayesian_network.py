from week8.bayesian_network.node import Node

class BayesianNetwork:

    def __init__(self):
        self.__nodes = {}

    def add_node(self, node: Node):
        self.__nodes.update({node.get_name(), node})

    def remove_node(self, node_name: str):
        del self.__nodes[node_name]