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

class BSTNode():
    def __init__(self, key: str, value: User = None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

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
        BSTNode.display_keys(self.right, space, level + 1)
        print(space * level + '->|' + str(self.key) + '|')
        BSTNode.display_keys(self.left,space, level + 1)

    def insert_bst(self, key: str, value: User):
        if self.key is None: 
            self.key = key
            return None
        elif self.key == key:
            print('Node already exists on the tree')
            return
        elif self.key > key:
            if self.left:
                self.left.insert_bst(key, value)
            else:
                self.left = BSTNode(key, value)
                self.left.parent = self
        elif self.key < key:
            if self.right:
                self.right.insert_bst(key, value)
            else:
                self.right = BSTNode(key, value)
                self.right.parent = self

    def find_node(self, key: str):
        if self.key is None:
            return None
        elif self.key == key:
            return self
        elif self.key > key:
            return BSTNode.find_node(self.left, key)
        elif self.key < key:
            return BSTNode.find_node(self.right, key)

if __name__ == '__main__':

    # Test Cases
    a = User('a', 'A...', 'a@example.com')
    b = User('b', 'B...', 'b@example.com')
    h = User('h', 'H...', 'h@example.com')
    j = User('j', 'J...', 'j@example.com')
    si = User('si', 'Si...', 'si@example.com')
    so = User('so', 'So...', 'so@example.com')
    v = User('v', 'V...', 'v@example.com')

    users = [j, b, so, a, h, si, v]

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
    database.update(User(username = 'a', name = 'Aa...', email = 'aa@example.com'))
    user = database.find('a')
    print(user)
    print('------------------------------------------------------------------------------------------')
    print('\n')

    print('---------------------- RETRIEVING THE LIST OF USERS ----------------------')
    print(database.list_all())
    print('--------------------------------------------------------------------------')
    print('\n')
    
    print('---------------------- ALPHABETICALLY ORDER SORTED -----------------------')
    database.insert(User(username = 'z', name = 'Z', email = 'z@example.com'))
    print(database.list_all())
    print('--------------------------------------------------------------------------')
    print('\n')

    print('---------------------- STORING KEYS USING BSTs ----------------------')
    tree = BSTNode(j.username, j)

    for user in users:
        tree.insert_bst(user.username, user)

    tree.display_keys()
    print('\n')

    print('---------------------- FIND NODE USING BSTs ----------------------')
    node = tree.find_node('h')
    print(node.key, node.value)
    print('\n')

    """
    tree = BSTNode(aakash)
    tree.display_keys()

    users = [biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]

    for user in users:
        tree.insert_bst(user.username, user)

    tree.display_keys()

    for i in list:
        tree.insert_bst(i)

    tree.display_keys()

    tree = BSTNode(None)
    list = [20, 4, 30, 4, 1, 5, 6]
    for i in list:
        tree.insert_bst(i)
    
    tree.display_keys()

    # print(users[0].username)
    tree = BSTNode(users[0].username, users[0])
    print(tree.key, tree.value)

    tree.left = BSTNode(users[1].username, users[1])
    tree.right = BSTNode(users[2].username, users[2])
    tree.display_keys()
    
    tree.left.left = BSTNode(users[3].username, users[3])
    tree.left.right = BSTNode(users[4].username, users[4])

    tree.right.left = BSTNode(users[5].username, users[5])
    tree.right.right = BSTNode(users[6].username, users[6])
    
    tree.display_keys()
    """
    print('\n')
