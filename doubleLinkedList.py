# Doubly LinkedList - ChatGPT

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_at_head(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
    def add_at_tail(self, data):
        new_node = Node(data)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def remove(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return
        if self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            return
        current = self.head.next
        while current and current.data != data:
            current = current.next
        if current:
            current.prev.next = current.next
            current.next.prev = current.prev
    
    def print_list(self):
        current = self.head
        print('\n')
        while current:
            print(current.data, end=' ')
            current = current.next


my_list = DoublyLinkedList()
my_list.add_at_head(5)
my_list.add_at_head(3)
my_list.add_at_tail(7)
my_list.print_list()  # Output: 3 5 7
my_list.remove(5)
my_list.print_list()  # Output: 3 7
