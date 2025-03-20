import unittest
from week8.bayesian_network.node import Node

class TestNode(unittest.TestCase):

    def test_add_parent(self):
        child_node = Node("child node")
        parent_node = Node("parent node")
        child_node.add_parent(parent_node)

        TestNode.assertEqual(self, child_node.parents[0], parent_node, "Parent node not in child node as expected.")
