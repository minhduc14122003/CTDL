class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Example usage
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_front(1)
    linked_list.insert_at_front(2)
    linked_list.insert_at_front(3)
    linked_list.insert_at_front(4)
    linked_list.insert_at_front(5)
    linked_list.insert_at_front(6)

    print("After inserting nodes at their front:", end=" ")
    linked_list.print_list()
