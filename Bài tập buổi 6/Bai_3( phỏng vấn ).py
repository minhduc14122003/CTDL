class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 1

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

    def partition(self, x):
        lessThanList = LinkedList()
        greaterThanEqualList = LinkedList()
        currentNode = self.head
        while currentNode:
            if currentNode.value < x:
                lessThanList.append(currentNode.value)
            else:
                greaterThanEqualList.append(currentNode.value)
            currentNode = currentNode.next
        # Concatenate the two lists
        lessThanList.tail.next = greaterThanEqualList.head
        greaterThanEqualList.tail.next = None
        return lessThanList

    def __str__(self):
        tempNode = self.head
        result = ''
        while tempNode is not None:
            result += str(tempNode.value)
            if tempNode.next is not None:
                result += " -> "
            tempNode = tempNode.next
        return result


list = LinkedList()
list.append(11)
list.append(3)
list.append(9)
list.append(10)
list.append(15)
x = 10
partitionList = list.partition(x)
print(partitionList.__str__())