
class Heap:
    def __init__(self, size: int):
        self.custom_list = (size + 1) * [None]
        self.heap_size = 0
        self.max_size = size + 1

def peek_of_heap(root_node: Heap):
    if root_node is None:
        return None
    return root_node.custom_list[1] 

def size_of_heap(root_node: Heap):
    if root_node is None:
        return None
    return root_node.heap_size 

def level_order_traversal(root_node: Heap)-> float:
    if root_node is None:
        return None
    for i in range(1, root_node.heap_size - 1):
        print(root_node.custom_list[i])

def is_full(root_node: Heap)-> bool:
    if root_node.heap_size + 1 == root_node.max_size:
        return True
    return False

def is_empty(root_node: Heap)-> bool:
    if root_node.heap_size == 0:
        return True
    return False

def heapify_tree_insert(root_node: Heap, index: int, heap_type: str):
    parent_index = index // 2
    if index <= 1:
        return None
    elif heap_type == 'Min':
        if root_node.custom_list[index] < root_node.custom_list[parent_index]:
            temp = root_node.custom_list[index]
            root_node.custom_list[index] = root_node.custom_list[parent_index]
            root_node.custom_list[parent_index] = temp
        heapify_tree_insert(root_node, parent_index, heap_type)
    elif heap_type == 'Max':
        if root_node.custom_list[index] > root_node.custom_list[parent_index]:
            temp = root_node.custom_list[index]
            root_node.custom_list[index] = root_node.custom_list[parent_index]
            root_node.custom_list[parent_index] = temp
        heapify_tree_insert(root_node, parent_index, heap_type)

def insert_node(root_node: Heap, node_value: int, heap_type: str)-> str:
    if is_full(root_node):
        return 'The Binary Heap is full'
    root_node.custom_list[root_node.heap_size + 1] = node_value
    root_node.heap_size += 1
    heapify_tree_insert(root_node, root_node.heap_size, heap_type)
    return 'The value has been successfully inserted'

def heapify_tree_extract(root_node: Heap, index: int, heap_type: str):
    left_index = index * 2
    right_index = index * 2 + 1
    swap_child = 0

    if root_node.heap_size < left_index: #no childs?
        return None
    elif root_node.heap_size == left_index: #only one child (last child)
        if heap_type == 'Min':
            if root_node.custom_list[index] > root_node.custom_list[left_index]:
                temp = root_node.custom_list[index]
                root_node.custom_list[index] = root_node.custom_list[left_index]
                root_node.custom_list[left_index] = temp
            return
        elif heap_type == 'Max':
            if root_node.custom_list[index] < root_node.custom_list[left_index]:
                temp = root_node.custom_list[index]
                root_node.custom_list[index] = root_node.custom_list[left_index]
                root_node.custom_list[left_index] = temp
            return
    else: # left and right child
        if heap_type == 'Min':
            if root_node.custom_list[left_index] < root_node.custom_list[right_index]:
                swap_child = left_index
            else:
                swap_child = right_index
            if root_node.custom_list[index] > root_node.custom_list[swap_child]:
                temp = root_node.custom_list[index]
                root_node.custom_list[index] = root_node.custom_list[swap_child]
                root_node.custom_list[swap_child] = temp
        if heap_type == 'Max':
            if root_node.custom_list[left_index] > root_node.custom_list[right_index]:
                swap_child = left_index
            else:
                swap_child = right_index
            if root_node.custom_list[index] < root_node.custom_list[swap_child]:
                temp = root_node.custom_list[index]
                root_node.custom_list[index] = root_node.custom_list[swap_child]
                root_node.custom_list[swap_child] = temp
    heapify_tree_extract(root_node, swap_child, heap_type)

def extract_node(root_node: Heap, heap_type: str)-> float:
    if is_empty(root_node):
        return 'The Binary Heap is empty'
    else:
        extracted_node = root_node.custom_list[1] #always the first
        root_node.custom_list[1] = root_node.custom_list[root_node.heap_size]
        root_node.custom_list[root_node.heap_size] = None
        root_node.heap_size -= 1
        heapify_tree_extract(root_node, 1, heap_type)
        return extracted_node

def delete_entire_bp(root_node):
    root_node.custom_list = None

if __name__ == '__main__':
    new_binary_heap = Heap(5)

    insert_node(new_binary_heap, 4, 'Max')
    insert_node(new_binary_heap, 5, 'Max')
    insert_node(new_binary_heap, 2, 'Max')
    insert_node(new_binary_heap, 1, 'Max')


    for i in range(10):
        print(insert_node(new_binary_heap, i, 'Max'))

    print(size_of_heap(new_binary_heap))
    delete_entire_bp(new_binary_heap)
    level_order_traversal(new_binary_heap) 