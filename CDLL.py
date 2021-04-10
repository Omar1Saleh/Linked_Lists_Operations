class Node:
    def __init__(self, value=None):
        self.prev = None
        self.value = value
        self.next = None


# DLL operations class
class Circular_Doubly_Linked_list:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        temp_node = self.head
        while temp_node:
            yield temp_node
            temp_node = temp_node.next
            if temp_node == self.tail.next:
                break

    def cdll_creation(self, value):
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            new_node.prev = new_node
            new_node.next = new_node
            print('list created!')
        else:
            print("DL/Linked_Lists_OperationsL already exists!")

    def insert_to_cdll(self, value, location):
        if self.head is None:
            return 'This list does n`t exist!'
        else:
            new_node = Node(value)
            if location == 0:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.head = new_node
                self.tail.next = new_node
            elif location == -1:
                new_node.next = self.head
                new_node.prev = self.tail
                self.tail.next = new_node
                self.head.prev = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.prev = temp_node
                new_node.next = next_node
                next_node.prev = new_node

    def traversal(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.tail.next:
                break

    def remove_list(self):
        self.head = None
        self.tail = None

    def reverse_traversal(self):
        temp_node = self.tail
        while temp_node:
            print(temp_node.value)
            temp_node = temp_node.prev
            if temp_node == self.head.prev:
                break

    def deletion_list(self, location):
        if self.head is None:
            return "This list doesn`t exist!"
        else:
            if self.head == self.tail:
                self.head.prev = None
                self.head.next = None
                self.head = None
                self.tail = None
            elif location == 0:
                self.head = self.head.next
                self.head.prev = self.tail
            elif location == -1:
                self.tail = self.tail.prev
                self.tail.next = self.head
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                temp_node.next = temp_node.next.next
                if temp_node.next is None:
                    self.tail = temp_node
                    self.tail.next = self.head
                else:
                    temp_node.next.prev = temp_node

    def search_list(self, value):
        temp_node = self.head
        while temp_node:
            if temp_node.value == value:
                return value
            else:
                temp_node = temp_node.next
                if temp_node == self.tail.next:
                    return  'valus not in list! '
