class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def traversal(self):
        if self.head is None:
            print("Linkedlist is empty")
        else:
            h = self.head
            while h is not None:
                print(h.data)
                h = h.ref    
                
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node