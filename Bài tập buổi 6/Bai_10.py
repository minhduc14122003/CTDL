class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
    def __str__(self):
        current = self.head
        res = ''
        while current is not None:
            res += f'{current.data} '
            current = current.next  
        return res
    
def removeDuplicate(new_list: LinkedList):
    status = {}
    current = new_list.head
    status[current.data] = 1
    while current.next is not None:
        if status.get(current.next.data) == 1:
            current.next = current.next.next
        else:
            status[current.next.data] = 1
            current = current.next

new_list = LinkedList()
new_list.append(1) 
new_list.append(2)
new_list.append(4)
new_list.append(3)
new_list.append(4)
new_list.append(2)
print(new_list)
removeDuplicate(new_list)
print(new_list)

