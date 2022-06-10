from binary_tree_demo import TreeNode

def is_binary_search_tree(root: TreeNode) -> bool:

    def valid(node: TreeNode, left_value, right_value):
        if node is None:
            return True
        if not (node.key < right_value and node.key > left_value):
            return False
        print('Current Tree: ', node, ', Min Value: ', left_value, ', Max Value: ', right_value)

        return (valid(node.left, left_value, node.key) and valid(node.right, node.key, right_value))
    return valid(root, float('-inf'), float('+inf'))

if __name__ == '__main__':
    print('---------------------- CHECK BINARY SEARCH TREE ----------------------')
    tree = TreeNode.parse_tuple(((0, 1, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
    tree.display_keys()
    print('IS BINARY SEARCH TREE?', is_binary_search_tree(tree))
    tree = TreeNode.parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
    print('IS BINARY SEARCH TREE?', is_binary_search_tree(tree))