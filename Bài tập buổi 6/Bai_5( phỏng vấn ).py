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

    def getIntersectionNode(self, head1, head2):
        def getLengthAndTail(head):
            length = 0
            tail = None
            while head:
                length += 1
                tail = head
                head = head.next
            return length, tail

        len1, tail1 = getLengthAndTail(head1)
        len2, tail2 = getLengthAndTail(head2)

        # If the tails are different, there is no intersection
        if tail1 != tail2:
            return None

        diff = abs(len1 - len2)

        # Move the pointers of the longer list forward
        longer = head1 if len1 > len2 else head2
        shorter = head2 if len1 > len2 else head1
        for _ in range(diff):
            longer = longer.next

        # Traverse both lists together until an intersection is found
        while longer != shorter:
            longer = longer.next
            shorter = shorter.next

        # Return the intersecting node (or None if there's no intersection)
        return longer

    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            self.tail.next = newNode
        self.tail = newNode
        self.length += 1


# Example usage
# Construct two linked lists
list1 = LinkedList(3)
list1.append(1)
list1.append(5)
list1.append(9)
list1.append(7)
list1.append(2)
list1.append(1)


list2 = LinkedList(2)
list2.append(4)
list2.append(6)
list2.append(7)
list2.append(2)
list2.append(1)

# Determine if the lists intersect and return the intersecting node
intersectingNode = LinkedList(0).getIntersectionNode(list1.head, list2.head)
if intersectingNode:
    print("Intersecting node value:", intersectingNode.value)
else:
    print("The lists do not intersect")