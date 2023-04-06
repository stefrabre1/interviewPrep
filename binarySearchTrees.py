# BST practice

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class binarySearchTree:
    def __init__(self):
        self.top = None
        
    def getTop(self):
        return self.top
        
    def insert(self, node):
        if self.top is None:
            self.top = node
        else:
            self.rInsert(self.top, node)
            
    def rInsert(self, rNode, nodeToAdd):
        if nodeToAdd.data < rNode.data:
            if rNode.left is not None:
                self.rInsert(rNode.left, nodeToAdd)
            else:
                rNode.left = nodeToAdd
        elif nodeToAdd.data > rNode.data:
            if rNode.right is not None:
                self.rInsert(rNode.right, nodeToAdd)
            else:
                rNode.right = nodeToAdd
                
    def printTree(self):
        if self.top is not None:
            self.rPrintTree(self.top)
    
    def rPrintTree(self, node):
        if node is not None:
            self.rPrintTree(node.left)
            print(str(node.data) + ' ')
            self.rPrintTree(node.right)
       
    def findInTree(self, val):
        if self.top is not None:
            return rFindInTree(self.top, val)
    
    def rFindInTree(self, rNode, val):
        if rNode.data == val:
            return true
        self.rFindInTree(rNode.left, val)
        self.rFindInTree(rNode.right, val)

        return false
       
## main 
#TODO This isn't working. Work on it more
bst = binarySearchTree()
bst.insert(Node(5))
bst.insert(Node(3))
bst.insert(Node(4))
bst.insert(Node(7))
bst.insert(Node(1))
bst.insert(Node(9))

bst.printTree()
print(bst.findInTree(4))
print(bst.findInTree(11))
