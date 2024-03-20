class BinarySearchTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def contains(self, target):
        temp = self.root
        while temp:
            if target < temp.value:
                temp = temp.left
            elif target > temp.value:
                temp = temp.right
            else:
                return True
        return False
