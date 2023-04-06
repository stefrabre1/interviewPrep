# BST practice

import sys
sys.setrecursionlimit(1500)

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
            if self.rFindInTree(self.top, val) is not None:
                return True
            return False
    
    def rFindInTree(self, rNode, val):
        if rNode.data == val:
            return rNode
        elif rNode.data > val and rNode.left is not None:
            return self.rFindInTree(rNode.left, val)
        elif rNode.data < val and rNode.right is not None:
            return self.rFindInTree(rNode.right, val)

       
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
