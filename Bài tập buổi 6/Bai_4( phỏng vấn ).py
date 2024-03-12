class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
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

    def get(self, index):
        if index >= self.length or index < 0:
            return None
        tempNode = self.head
        for _ in range(index):
            tempNode = tempNode.next
        return tempNode

    def getReverseSum(self, list):
        sum = 0
        for i in range(list.length-1, -1, -1):
            sum += list.get(i).value * pow(10, i)
        return sum

    def sumLists(self, list1, list2):
        sum1 = LinkedList().getReverseSum(list1)
        sum2 = LinkedList().getReverseSum(list2)
        sums = sum1+sum2
        while sums > 1:
            self.append(int(sums % 10))
            sums /= 10

    def __str__(self):
        tempNode = self.head
        result = ''
        while tempNode is not None:
            result += str(tempNode.value)
            if tempNode.next is not None:
                result += " -> "
            tempNode = tempNode.next
        return result


list1 = LinkedList()
list1.append(7)
list1.append(1)
list1.append(6)

list2 = LinkedList()
list2.append(5)
list2.append(9)
list2.append(2)

list = LinkedList()
list.sumLists(list1, list2)
print(list.__str__())