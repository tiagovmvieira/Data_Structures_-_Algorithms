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
    def __init__(self, key, value = None):
        self.key = key
        self.value = value 
        self.left = None
        self.right = None
        self.parent = None

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

    print('---------------------- STORING KEY-VALUE PAIRS USING BSTs ----------------------')
    print('\n')
