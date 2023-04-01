# doubly linked lists practice

class Node:        
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
    def __repr__(self):
        return self.data
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        
        while node is not None:
            nodes.append(node.data)
            node = node.next
            
        nodes.append("None")    
        return " <-> ".join(nodes)
    
## main 

dllist = DoublyLinkedList()
dllist.head = Node("1")
node2 = Node("2")
node3 = Node("3") 

dllist.head.next = node2
node2.prev = dllist.head
node2.next = node3
node3.prev = node2

print(dllist.__repr__())