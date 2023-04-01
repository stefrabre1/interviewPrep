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

for node in llist:
    print(node)

## My own attempt
# def node(x):
    # content = x 
    # nextNode = Null
    # return content, nextNode
    
# def search(x):
    # idx = 0
    # tempNode = node(-1) #todo: change this to not be -1 (head node)
    # while temp.content != x:
        # idx += 1
        # tempNode = tempNode.nextNode
        
        # if tempNode.nextNode == Null:
            # return -1
    # return idx
    
# def delete(idx):
    # temp = 0
    # tempNode = node(-1) #todo: change this to not be -1 (head node)
    
    # while temp < idx:
        # temp += 1
        # tempNode = tempNode.nextNode
    # tempNode.nextNode = tempNode.nextNode.nextNode
