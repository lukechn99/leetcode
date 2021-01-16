class Node:
    def __init__(self, val = None):
        self.next = None
        self.val = val
    
    def append(self, val):
        n = self.next
        while self.next != None:
            n = self.next
        n.next = Node(val)

