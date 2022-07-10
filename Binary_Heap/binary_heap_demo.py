
class Heap:
    def __init__(self, size: int):
        self.custom_list = (size + 1) * [None]
        self.heap_size = 0
        self.max_size = size + 1

    def peek_of_heap(root_node: int):
        if root_node is None:
            return None
        return root_node.custom_list[1]


if __name__ == '__main__':
    new_binary_heap = Heap(5)