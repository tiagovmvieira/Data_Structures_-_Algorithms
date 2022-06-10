class TreeNode:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None

    def to_tuple(self)-> tuple:
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left), self.key, TreeNode.to_tuple(self.right)

    def __repr__(self)-> str:
        return 'BINARY TREE ->{}<-'.format(self.to_tuple())

    def __str__(self)-> str:
        return self.__repr__()

    def display_keys(self, space: str = '\t', level: int = 0):
        #print(self.key if self else None, level)
        # If the node is empty
        if self is None:
            print(space * level + '->|' + '∅' + '|')
            return # Terminate recursion
        
        # If the node is a leaf
        if self.left is None and self.right is None:
            print(space * level + '->|' + str(self.key) + '|')
            return # Terminate recursion

        # If the node has children
        TreeNode.display_keys(self.right, space, level + 1)
        print(space * level + '->|' + str(self.key) + '|')
        TreeNode.display_keys(self.left,space, level + 1)    

    def tree_height(self)-> int:
        if self is None:
            return 0
        return 1 + max(TreeNode.tree_height(self.left) , TreeNode.tree_height(self.right))

    def tree_size(self)-> int:
        if self is None:
            return 0
        return 1 + TreeNode.tree_size(self.left) + TreeNode.tree_size(self.right)

    def traverse_in_order(self)-> list:
        if self is None:
            return []
        return (TreeNode.traverse_in_order(self.left) + [self.key] + TreeNode.traverse_in_order(self.right))

    def traverse_in_preorder(self)-> list:
        if self is None:
            return []
        return ([self.key] + TreeNode.traverse_in_preorder(self.left) + TreeNode.traverse_in_preorder(self.right))

    @staticmethod
    def parse_tuple(data: tuple):
        #print(data)
        if isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0]) # recursion
            node.right = TreeNode.parse_tuple(data[2]) # recursion
        elif data is None:
            node = None
        else:
            node = TreeNode(data)
        return node

if __name__ == '__main__':

    print('---------------------- BINARY TREE ----------------------')
    tree = TreeNode.parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
    print(tree.__str__())
    print('\n')
    tree.display_keys()
    print('\n')
    print('TREE HEIGHT:', tree.tree_height())
    print('TREE SIZE:', tree.tree_size())
    print('\n')
    print('TRAVERSE IN ORDER', tree.traverse_in_order())
    print('TRAVERSE IN PREORDER', tree.traverse_in_preorder())
    print('\n')