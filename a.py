class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


node = TreeNode(3)

def display_keys(node):
    if node.left is None and node.right is None:
        print(str(node.key))
    return

display_keys(node)