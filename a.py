users = ['A', 'B', 'C', 'D', 'E', 'F']
i = 0
user = 'G'

while i < len(users):
    if users[i] > user:
        break
    i += 1
users.insert(i, 'G')

print(users)