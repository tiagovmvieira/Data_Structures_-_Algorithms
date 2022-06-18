from typing import Union

def get_index(data_list: list, a_string: str)-> int:
    result = 0

    for a_character in a_string:
        a_number = ord(a_character)
        result += a_number

    list_index = result % len(data_list)
    return list_index

class BasicHashTable:
    def __init__(self, max_hash_table_size: int):
        self.data_list = [None] * max_hash_table_size

    def get_index(self, key: str)-> int:
        result  = 0

        for a_character in key:
            a_number = ord(a_character)
            result += a_number

        list_index = result % len(self.data_list)
        return list_index
    
    def insert(self, key: str, value: str):
        index = self.get_index(key)

        self.data_list[index] = (key, value)

    def find(self, key: str)-> Union[None, str]:
        index = self.get_index(key)

        kv = self.data_list[index]
        if kv is None:
            return None
        else:
            key, value = kv
            return value

    def update(self, key: str, value: str):
        index = self.get_index(key)

        self.data_list[index] = (key, value)

    def list_all(self)-> str:
        return [kv[0] for kv in self.data_list if kv is not None]

if __name__ == '__main__':
    print('---------------------- NAIVE HASH TABLE ----------------------')
    MAX_HASH_TABLE_SIZE = 4096

    data_list = [None] * MAX_HASH_TABLE_SIZE
    len(data_list)

    print('---------------------- HASHING FUNCTION ----------------------')
    print(get_index(data_list, 'aaa'))

    print('---------------------- HASH TABLE INSERTION ----------------------')
    data_list[get_index(data_list, 'aaa')] = ('aaa', '123')
    print(data_list[get_index(data_list, 'aaa')])

    print('---------------------- HASH TABLE FIND ----------------------')
    index = get_index(data_list, 'aaa')
    index, value = data_list[index]
    print(value)

    print('---------------------- HASH TABLE LIST ALL ----------------------')
    pairs = [kv[0] for kv in data_list if kv is not None]
    print(pairs)
    print('\n')

    print('---------------------- HASH TABLE IMPLEMENTATION ----------------------')
    hash_table = BasicHashTable(4096)

    print('---------------------- HASH TABLE INSERTION ----------------------')
    hash_table.insert('aaa', '123')

    print('---------------------- HASH TABLE FIND ----------------------')
    print(hash_table.find('aaa'))

    print('---------------------- HASH TABLE UPDATE ----------------------')
    hash_table.update('aaa', '456')

    print('---------------------- HASH TABLE LIST ALL ----------------------')
    print(hash_table.list_all())
    print('\n')
