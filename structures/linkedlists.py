class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def traversal(self):
        first = self.head
        while first:
            print(first.data)
            first = first.next

    def insert_new_header(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def search(self, x):
        temp = self.head
        while temp is not None:
            if temp.data == x:
                return True
            temp = temp.next
        else:
            return False
        
    def delete_node(self, data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
        prev.next = temp.next

    def delete_tail_node(self):
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None


family = LinkedList()
family.head = Node("Bob")
wife = Node("Amy")
first_kid = Node("Max")
second_kid = Node("Jenny")

family.head.next = wife
wife.next = first_kid
first_kid.next = second_kid

print("The family:")
family.traversal()

print("...adding Dave")
family.insert_new_header("Dave")
print("\n is Bob still there?...")
family.traversal()

print("\n removing Bob")
family.delete_node("Bob")
family.traversal()

print("\n Adding Alex")
family.insert_new_header("Alex")
family.traversal()

print("\n removing Amy")
family.delete_node("Amy")
family.traversal()

print("\n removing tail")
family.delete_tail_node()
family.traversal()
