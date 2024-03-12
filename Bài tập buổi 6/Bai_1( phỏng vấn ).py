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

    def removeDuplicates(self):
        if self.head is None:
            return
        nodeValues = set()  # set to store unique node values
        currentNode = self.head
        nodeValues.add(currentNode.value)
        while currentNode.next:
            if currentNode.next.value in nodeValues:  # duplicate found
                currentNode.next = currentNode.next.next
                self.length -= 1
            else:
                nodeValues.add(currentNode.next.value)
                currentNode = currentNode.next
        self.tail = currentNode

    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            self.tail.next = newNode
        self.tail = newNode
        self.length += 1

    def delete(self, index):
        preNode = self.head
        if index >= self.length or index <= -1:
            return None
        if index == 0:
            return self.popFirst()
        if index == self.length-1:
            return self.pop()
        for _ in range(index-1):
            preNode = preNode.next
        deletedNode = preNode.next
        preNode.next = deletedNode.next
        deletedNode.next = None
        self.length -= 1
        return deletedNode

    def __str__(self):
        tempNode = self.head
        result = ''
        while tempNode is not None:
            result += str(tempNode.value)
            if tempNode.next is not None:
                result += " -> "
            tempNode = tempNode.next
        return result


list = LinkedList(1)
list.append(2)
list.append(2)
list.append(3)
list.append(4)
list.append(4)
list.append(4)
list.append(5)
list.removeDuplicates()
print(list.__str__())