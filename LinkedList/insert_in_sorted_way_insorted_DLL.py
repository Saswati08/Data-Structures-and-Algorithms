class node:
    def __init__(self, val):
        self.data = val
        self.next = None
	self.prev = None

def sortedInsert(head, x):
    #code here
    if head == None:
        nw = Node(x)
        head = nw
        return head
        
    
    curr = head
    while(curr.next != None and curr.data < x):
        curr = curr.next
        
    nw = Node(x)
    if curr.next == None:
        if curr.data < x:
            nw.prev = curr
            curr.next = nw
            return head
    
        
    if curr == head:
        if curr.data < x:
            curr.next = nw
            nw.prev = curr
            return head
        else:
            nw.next = curr
            curr.prev = nw
            head = nw
            return head
    nw.prev = curr.prev
    if curr.prev:
        curr.prev.next = nw
        curr.prev = nw 
    nw.next = curr
    return head
    

nw = node(1)
nw2 = node(2)
nw.next = nw2
nw2.prev = nw
nw3 = node(3)
nw3.prev = nw2
nw2.next = nw3
sortedInsert(nw, 4)
