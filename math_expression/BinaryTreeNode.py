class BinaryTreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.operator = False

    def is_leaf(self) -> bool:
        return (self.left is None) and (self.right is None) 