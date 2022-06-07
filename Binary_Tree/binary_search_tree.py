from ctypes.wintypes import BOOLEAN
from xmlrpc.client import Boolean
from binary_tree_demo import TreeNode

def is_binary_search_tree(node: TreeNode)-> Boolean:
    pass

if __name__ == '__main__':
    print('---------------------- CHECK BINARY SEARCH TREE ----------------------')
    tree = TreeNode.parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))