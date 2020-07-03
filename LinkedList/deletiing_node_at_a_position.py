class node:
    def __init__(self, val):
        self.data = val
        self.next = None

def delNode(head, k):
    # Code here
    
    if k == 1:
        head = head.next
        return head
        
    curr = head
    c = 1
    while(curr != None and c < k - 1):
        curr = curr.next
        c += 1
    
        
    
    curr.next = curr.next.next
    
    return head

nw = node(1)
nw.next = node(2)
nw.next.next = node(4)
nw.next.next.next = node(5)
nw.next = None

hd = delNode(nw, 3)
temp = hd

while(temp!= None):
	print(temp.data)
	temp = temp.next

