from __future__ import annotations

class TreeNode:
    def __init__(self, data: int, children: list = []):
        self.data = data
        self.children = children

    def __str__(self, level: int = 0):
        ret = "  " * level + str(self.data)  + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def add_child(self, tree_node: TreeNode):
        self.children.append(tree_node)