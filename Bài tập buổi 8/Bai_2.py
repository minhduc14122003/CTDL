class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
newBinaryTree = TreeNode('Drink:')
leftChild = TreeNode('Hot')
rightChild = TreeNode('Cold')
newBinaryTree.leftChild = leftChild
newBinaryTree.rightChild = rightChild

def PreOderTraverse(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    PreOderTraverse(rootNode.leftChild)
    PreOderTraverse(rootNode.rightChild)

def InOderTraverse(rootNode):
    if not rootNode:
        return
    InOderTraverse(rootNode.leftChild)
    print(rootNode.data)
    InOderTraverse(rootNode.rightChild)  

def PostOderTraverse(rootNode):
    if not rootNode:
        return
    PostOderTraverse(rootNode.leftChild)
    PostOderTraverse(rootNode.rightChild)    
    print(rootNode.data)

def LevelOderTraverse(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)   
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)

LevelOderTraverse(newBinaryTree)             


        