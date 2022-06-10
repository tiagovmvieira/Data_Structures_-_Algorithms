class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val: int):
        if self.head is None:
            self.head = Node(val)
        else:
            iterator = self.head #iterator starts on the head
            while iterator.next is not None:
                iterator = iterator.next # pointing 
            iterator.next = Node(val) # appending

    def append_by_position(self, node: Node, position: int):
        iterator = self.head #iterator start on the head
        if position == 0:
            self.head = node
            self.head.next = iterator
        else:
            i = 1
            while iterator is not None:
                if i == position:
                    historic = iterator.next
                    iterator.next = node
                    iterator.next.next = historic
                i += 1
                iterator = iterator.next

    def print(self)-> str:
        if self.head is None:
            print('Linked list is empty')
            return

        iterator = self.head # iterator starts on the head
        linked_list_string = '' # starts empty
        
        while iterator is not None:
            linked_list_string += str(iterator.val) + '-->'
            iterator = iterator.next
        
        linked_list_string = linked_list_string[:-3]
        print(linked_list_string)

    def get_length(self)-> int:
        result = 0
        if self.head is None:
            return result

        iterator = self.head
        while iterator is not None:
            result += 1
            iterator = iterator.next
        return result

    def find_element(self, position: int)-> int:
        i = 0
        iterator = self.head 
        while iterator is not None:
            if i == position:
                return iterator.val
            iterator = iterator.next 
            i += 1

    def reverse_linked_list(self): #iteratively
        if self.head is None:
            print('Linked List is empty')
            return 

        iterator = self.head
        previous_node = None

        while iterator is not None:
            historic = iterator.next # storing the historic forward
            iterator.next = previous_node # flipping the pointer

            previous_node = iterator # looping
            iterator = historic # looping
        self.head = previous_node
        
if __name__ == '__main__':

    nodes = []
    for i in range(1, 11):
        nodes.append(Node(i))

    linked_list = LinkedList()

    for i,j in enumerate(nodes):
        linked_list.append(nodes[i].val)

    print('---------------------- LINKED LIST ----------------------')
    linked_list.print()
    linked_list.find_element(2)

    new_node_A = Node(0)
    new_node_B = Node(99)

    linked_list.append_by_position(new_node_A, 0)
    linked_list.print()

    linked_list.append_by_position(new_node_B, 12)
    linked_list.print()

    linked_list.reverse_linked_list()
    linked_list.print()