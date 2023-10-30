from __future__ import annotations
class Node:
    def __init__(self, data, next_node: Node | None):
        self._data = data
        self._next_node = next_node

    def set_next(self, node: Node | None):
        self._next_node = node

    def get_next(self) -> Node | None:
        return self._next_node

    def get_data(self):
        return self._data


class Stack:
    def __init__(self):
        self._head_node = None
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def push(self, data):
        node = Node(data, self._head_node)
        self._head_node = node
        self._size += 1

    def pop(self):
        # if self._size == 0:
            # return None

        if self._head_node is not None:
            return_data = self._head_node.get_data()
            self._head_node = self._head_node.get_next()
            self._size -= 1
            return return_data
        else:
            raise Exception("Attempt to access empty node")

    def top(self):
        if self._size == 0:
            return None
        return self._head_node.get_data()


    def is_empty(self):
        return self._size == 0

    def __str__(self):
        ret_str = '['
        node = self._head_node
        while node:
            ret_str += str(node.get_data())
            node = node.get_next()
            if node:
                ret_str += ', '
        ret_str += ']'
        return ret_str


my_stack = Stack()

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print(my_stack, len(my_stack))

print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())

# while not my_stack.is_empty():
#     print(my_stack.pop())

