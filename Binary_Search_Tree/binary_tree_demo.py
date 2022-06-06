from select import KQ_FILTER_AIO


class User:
    def __init__(self, username: str, name: str, email: str):
        self.username = username
        self.name = name
        self.email = email
    
    def __repr__(self):
        return "User(username = '{}', name='{}', email='{}')".format(self.username, self.name, self.email)

    def __str__(self):
        return self.__repr__()

class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user: User):
        i = 0
        while i < len(self.users):
            # Find the first username greater than the new user's username
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user) #.insert() list method

    def find(self, username: str):
        for user in self.users:
            if user.username == username:
                return user
            return 'User Not Found'

    def update(self, user: User):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self)-> list:
        return self.users

class TreeNode:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None

    def display_keys(self, space: str = '\t', level: int = 0):
        #print(self.key if self else None, level)
        
        # If the node is a leaf
        if self.left is None and self.right is None:
            print(space * level + '|' + str(self.key) + '|<-')
            return # Terminate recursion

        # If the node has a right children
        if self.right is not None:
            self.right.display_keys(space, level + 1)
        else: # if the node is empty
            print(space * (level + 1) + '|' + '∅' + '|<-')

        print(space * level + '|' + str(self.key) + '|<-')

        # If the node has a left children 
        if self.left is not None:
            self.left.display_keys(space, level + 1)
        else: # if the node is empty
            print(space * (level + 1) + '|' + '∅' + '|<-')

    def tree_height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.tree_height(self.left) , TreeNode.tree_height(self.right))

    def traverse_in_order(self):
        if self is None:
            return []
        return (TreeNode.traverse_in_order(self.left) + [self.key] + TreeNode.traverse_in_order())

def parse_tuple(data: tuple)-> TreeNode:
    #print(data)
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0]) # recursion
        node.right = parse_tuple(data[2]) # recursion
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

def tree_to_tuple(node: TreeNode):
    if node.left is None and node.right is None:
        return node.key
    elif node.right is None and node.left is not None:
        right = node.right
        key = node.key
        left = tree_to_tuple(node.left)
        print(key, right, left)
        return (left, key, right)
    elif node.left is None and node.right is not None:
        left = node.left
        key = node.key
        right = tree_to_tuple(node.right)
        print(key, right, left)
        return (left, key, right)

if __name__ == '__main__':
    
    # Test Cases
    users = []
    for i in range(7):
        users.append(User('example' + str(i), 'Example' + str(i), 'example' + str(i) + '@example.com'))

    print('---------------------- TEST CASES ----------------------')
    print(*users, sep = '\n')
    print('--------------------------------------------------------')
    print('\n')

    print('---------------------- SORTING THE INFO ON THE USERDB ----------------------')
    database = UserDatabase()
    for i in range(len(users)):
        database.insert(users[i])
    print('----------------------------------------------------------------------------')
    print('\n')

    print('---------------------- ACESSING AND UPDATING THE INFO ON THE USERDB ----------------------')
    user = database.find(users[0].username)
    print(user)
    database.update(User(username = 'example0', name= 'ExampleZero', email = 'examplezero@example.com'))
    user = database.find('example0')
    print(user)
    print('------------------------------------------------------------------------------------------')
    print('\n')

    print('---------------------- RETRIEVING THE LIST OF USERS ----------------------')
    print(database.list_all())
    print('--------------------------------------------------------------------------')
    print('\n')
    
    print('---------------------- ALPHABETICALLY ORDER SORTED -----------------------')
    database.insert(User(username = 'example7', name = 'Example7', email = 'example7@example.com'))
    print(database.list_all())
    print('--------------------------------------------------------------------------')
    print('\n')

    print('---------------------- BINARY TREE ----------------------')
    tree = parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
    tree.display_keys()
    print('TREE HEIGHT:', tree.tree_height())
    print('\n')

    print('---------------------- TRAVERSING A BINARY TREE ----------------------')
    print('-------------------------- INORDER TRAVERSAL -------------------------')
    # print(tree.traverse_in_order())

    print('---------------------- BINARY TREE ----------------------')
    print(tree.tree_height())
