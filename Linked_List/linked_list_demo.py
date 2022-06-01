class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beggining(self, data):
        node = Node(data, self.head)
        self.head = Node

    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return

        iterator = self.head
        linked_list_string = '' 
        
        while iterator:
            linked_list_string += str(iterator.data) + '-->'
            iterator = iterator.next
        
        print(linked_list_string)

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_at_beggining(5)
    linked_list.insert_at_beggining(89)
    linked_list.print()