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

    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            self.tail.next = newNode
        self.tail = newNode
        self.length += 1

    def get(self, index):
        if index >= self.length or index < 0:
            return None
        tempNode = self.head
        for _ in range(index):
            tempNode = tempNode.next
        return tempNode

    def findNthLastElements(self, nth):
        if nth > self.length:
            return None
        index = self.length - nth
        return self.get(index)


list = LinkedList(1)
list.append(2)
list.append(0)
list.append(3)
list.append(5)
print(list.findNthLastElements(2).value)