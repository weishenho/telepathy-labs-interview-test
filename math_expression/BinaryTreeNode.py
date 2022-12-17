class BinaryTreeNode:
    def __init__(self, data, left=None, right=None, operator=False) -> None:
        self.data = data
        self.left = left
        self.right = right
        self.operator = operator

    def is_leaf(self) -> bool:
        return (self.left is None) and (self.right is None) 