class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def makeEmpty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
        else:
            self.tail.next = newNode

        self.tail = newNode
        self.length += 1


myLinkedList = LinkedList(1)
myLinkedList.makeEmpty()
myLinkedList.append(1)
myLinkedList.append(2)

print('Head:', myLinkedList.head.value)
print('Tail:', myLinkedList.tail.value)
print('Length:', myLinkedList.length, '\n')
print('Linked List:')
myLinkedList.printList()