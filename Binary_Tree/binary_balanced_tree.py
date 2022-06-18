from typing import Union
from binary_tree_demo import TreeNode
from binary_search_tree_app import BSTNode, User

def is_binary_balanced_tree(tree: Union[BSTNode, TreeNode])-> bool:

    def dfs(tree: Union[BSTNode, TreeNode])-> list:
        # print('Current Tree: ', tree)

        if tree is None:
            return [True, 0]
        
        left, right = dfs(tree.left), dfs(tree.right)
        balanced = (left[0] and right[0] and
                    abs(left[1] - right[1]) <= 1)

        return [balanced, 1 + max(left[1], right[1])]
    return dfs(tree)[0]

if __name__ == '__main__':
    print('---------------------- CHECK BINARY BALANCED TREE ----------------------')
    print('\n')

    print('---------------------- DEFAULT TREE ----------------------')
    tree = TreeNode.parse_tuple(((0, 1, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
    tree.display_keys()
    tree = TreeNode(None)
    tree.display_keys()
    print('IS BINARY BALANCED TREE?', is_binary_balanced_tree(tree))
    print('\n')

    print('---------------------- BINARY SEARCH TREE ----------------------')
    a = User('a', 'A...', 'a@example.com')
    b = User('b', 'B...', 'b@example.com')
    h = User('h', 'H...', 'h@example.com')
    j = User('j', 'J...', 'j@example.com')
    si = User('si', 'Si...', 'si@example.com')
    so = User('so', 'So...', 'so@example.com')
    v = User('v', 'V...', 'v@example.com')
    users = [b, so, a, h, si, v]

    tree = BSTNode(j.username, j)

    for user in users:
        tree.insert_bst(user.username, user)
    tree.display_keys()
    print('IS BINARY BALANCED TREE?', is_binary_balanced_tree(tree))
    print('\n')