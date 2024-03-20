class TreeNode:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children

    def __str__(self, level = 0 ):
        ret = "  " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def addChildren(self, TreeNode):
        self.children.append(TreeNode)

tree = TreeNode('Drink:', [])
cold = TreeNode('Cold:', [])
hot = TreeNode('Hot:', [])                                   
tree.addChildren(cold)
tree.addChildren(hot)
tea = TreeNode('Tea', [])
coffee = TreeNode('Coffee', [])
cola = TreeNode('Cola', [])
fanta = TreeNode('Fanta', [])
cold.addChildren(cola)
cold.addChildren(fanta)
hot.addChildren(tea)
hot.addChildren(coffee)
print(tree)




            


        
    