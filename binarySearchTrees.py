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
            self.rInsert(node)
            
    def rInsert(self, node):
        tempNode = self.top
        if node.data < tempNode.data:
            if node.left is not None:
                self.rInsert(node.left)
            else:
                print("is left happening?")
                node.left = node
        elif node.data > tempNode.data:
            if node.right is not None:
                self.rInsert(node.right)
            else:
                node.right = node
    
    def printTree(self, node):
        if node is not None:
            self.printTree(node.left)
            print(str(node.data) + ' ')
            self.printTree(node.right)
       
## main 
#TODO This isn't working. Work on it more
bst = binarySearchTree()
bst.insert(Node(5))
bst.insert(Node(3))
bst.insert(Node(4))
bst.insert(Node(7))
bst.insert(Node(1))
bst.insert(Node(9))

bst.printTree(bst.getTop())

# print(bst.__repr__())