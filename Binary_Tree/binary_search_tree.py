from binary_tree_demo import TreeNode

def remove_none(nums: list)-> list:
    return [v for v in nums if v is not None]

def is_binary_search_tree(node: TreeNode)-> tuple:
    if node is None:
        return True, None, None

    is_bst_l, min_l, max_l = is_binary_search_tree(node.left)
    is_bst_r, min_r, max_r = is_binary_search_tree(node.right)

    is_bst_node = (is_bst_l and is_bst_r and
                (max_l is None or node.key > max_l) and
                (min_r is None or node.key < min_r))

    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))

    print(node.key, min_key, max_key, is_bst_node)
    return (is_bst_node, min_key, max_key)

if __name__ == '__main__':
    print('---------------------- CHECK BINARY SEARCH TREE ----------------------')
    tree = TreeNode.parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
    print(is_binary_search_tree(tree))