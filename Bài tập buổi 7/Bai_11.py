class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value) -> None:
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

myLinkedList = LinkedList(4)
print('Head:', myLinkedList.head.value)
print('Tail:', myLinkedList.tail.value)
print('Length:', myLinkedList.length)