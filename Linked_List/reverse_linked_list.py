class Node():
    def __init__(self, number, next = None)-> None:
        self.data = number
        self.next = next
        
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)

print(node1.data, node2.data, node3.data)

class LinkedList():
    def __init__(self)-> None:
        self.head = None

    def append(self, value):
        if self.head is None: # if there is not an head
            self.head = Node(value) # append on the head
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value) # append

    def append_by_position(self, value, position)

    def show_elements(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

list1 = LinkedList()

list1.head = node1
list1.head.next = node2
list1.head.next.next = node3

print(list1.head.data, list1.head.next.data, list1.head.next.next.data)

list2 = LinkedList()
list2.append(2)
list2.append(3)
list2.append(4)

print(list2.head.data, list2.head.next.data, list2.head.next.next.data)
list2.show_elements()