# circular linked list practice

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return self.data
        
class CircularLinkedList:
    def __init__(self):
        self.head = None
        
    def __repr__(self):
        node = self.head
        nodes = []
        
        while node is not None:
            nodes.append(node.data)
            node = node.next
            if node == self.head:
                break
            
        return " -> ".join(nodes)
        
## main

cllist = CircularLinkedList()
cllist.head = Node("0")
node1 = Node("1")
node2 = Node("2") 

cllist.head.next = node1
node1.next = node2
node2.next = cllist.head

print(cllist.__repr__())