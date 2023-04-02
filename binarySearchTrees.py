# BST practice

class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        
class binarySearchTree:
    def __init__(self):
        self.top = None
        
    def insert(self, node):
        # empty tree
        if self.top is None:
            print("Yeah")
            self.top = node
            return
        
        temp = self.top
        
        while True: # lol
            if temp.data == node.data:
                raise Exception("Duplicate data found!")

            # left child 
            while temp.left is not None and node.data < temp.data:
                temp = temp.left
                
            # right child
            while temp.right is not None and node.data > temp.data:
                temp = temp.left
                
            # insertion
            if node.data < temp.data:
                temp.left = node
                node.parent = temp
                return
            elif node.data > temp.data:
                temp.right = node
                node.parent = temp
                return
                
## main 

bst = binarySearchTree()
bst.insert(Node(5))
bst.insert(Node(3))
bst.insert(Node(7))

