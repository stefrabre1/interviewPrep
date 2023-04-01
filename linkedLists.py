# linked list practice

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None
      
    def __repr__(self):
        node = self.head
        nodes = []
        
        while node is not None:
            nodes.append(node.data)
            node = node.next
        
        nodes.append("None")
        return " -> ".join(nodes)
        
    def __iter__(self):
        node = self.head
        
        while node is not None:
            yield node
            node = node.next
        
    # my own attempt at beginning insertion
    def insert_start(self, data):
        temp = self.head.data
        tempNode = self.head
        
        self.head = Node(data)
        self.head.next = tempNode
        tempNode.data = temp
        
    def add_first(self, node):
        node.next = self.head
        self.head = node
        
    # my own attempt to add to the end
    def insert_end(self, node):
        tempNode = self.head
        
        while tempNode.next is not None:
            tempNode = tempNode.next
            
        tempNode.next = node
        
    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node
        
    # my own attempt to add in the middle (after specified node)
    def insert_after(self, node, data):
        if self.head is None:
            print("List empty!")
            return
        
        tempNode = self.head    
            
        while tempNode.next is not None:
            if tempNode.data == data:
                tempNext = tempNode.next
                tempNode.next = node
                node.next = tempNext
                return
            tempNode = tempNode.next
        print("Node not found!")
        
    def add_after(self, to_find, new_node):
        if self.head is None:
            raise Exception("List is empty")
            
        for node in self:
            if node.data == to_find:
                new_node.next = node.next
                node.next = new_node
                return
                
        raise Exception("Node with data '%s' not found" % to_find)
        
    # my own attempt to add in the middle (before a specified node)
    def insert_before(self, new_node, data):
        if self.head is None:
            print("List is empty!")
            return
        
        previous = self.head
            
        for node in self:
            previous = node
            
            if node.next is not None and node.next.data == data:
                new_node.next = node.next
                node.next = new_node
                return
                
        print("Node not found!")

    def add_before(self, to_find, new_node):
        if self.head is None:
            raise Exception("List is empty")
            
        if self.head.data == to_find:
            return self.add_first(new_node)
            
        prev_noded = self.head
        
        for node in self:
            if node.data == to_find:
                prev_node.next = new_node
                new_node.next = node
                return
            
            prev_node = node
        
        raise Exception("Node with data '%s' not found" % to_find)
        
    # my own attempt at deleting a node
    def delete_node(self, to_delete):
        if self.head is None:
            raise Exception("List is empty!")
            
        # this won't find the first element in a list    
        for node in self:
            if node.next is not None and node.next.data == to_delete:
                node.next = node.next.next
                return
                
        raise Exception("Couldn't find '%s'!" % to_delete)   

    def remove_node(self, to_find):
        if self.head is None:
            raise Exception("List is empty")
            
        if self.head.data == to_find:
            self.head = self.head.next
            return
            
        prev_node = self.head
        for node in self:
            if node.data == to_find:
                prev_node.next = node.next
                return
            prev_node = node
            
        raise Exception("Node with data '%s' not found" % to_find)

## Main

llist = LinkedList()

nodeOne = Node("1")
llist.head = nodeOne
print(llist.__repr__())

nodeTwo = Node("2")
nodeThree = Node("3")
nodeOne.next = nodeTwo
nodeTwo.next = nodeThree
print(llist.__repr__())

llist.insert_start("0")
llist.insert_start("-1")

llist.add_first(Node("-2"))

llist.insert_end(Node("4"))

llist.add_last(Node("5"))

llist.insert_after(Node("2.5"), "2")

llist.add_after("4", Node("4.5"))

llist.insert_before(Node("0.5"), "1")

llist.add_before("2", Node("1.5"))

llist.delete_node("-1")

llist.remove_node("-2")

print(llist.__repr__())

for node in llist:
    print(node)
