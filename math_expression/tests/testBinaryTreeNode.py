import unittest
from BinaryTreeNode import BinaryTreeNode

class TestBinaryTreeNode(unittest.TestCase):
    def setUp(self):
        self.leaf_node =  BinaryTreeNode(None)

        self.node =  BinaryTreeNode("-")
        self.node.operator =  True
        self.node.left = BinaryTreeNode(2)
        self.node.right = BinaryTreeNode(1)

    def test_is_leaf(self):
        self.assertTrue(self.leaf_node.is_leaf())

    def test_is_not_leaf(self):
        self.assertFalse(self.node.is_leaf())

    def test_instance_of(self):
        self.assertIsInstance(self.node, BinaryTreeNode)

if __name__ == '__main__':
    unittest.main()