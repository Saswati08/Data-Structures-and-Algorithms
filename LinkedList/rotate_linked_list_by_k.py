class node:
    def __init__(self, val):
        self.data = val
        self.next = None


def rotateList(head, k):
    # code here
    if head.next == None:
        return head
    last = head
    c = 1
    
    while(last.next != None):
        if c == k:
            kth_node = last
        last = last.next
        c += 1
        
    k = k % c
    
    if k == 0:
        return head
    
    nw_head = kth_node.next   
    kth_node.next = None
    last.next = head
    
    return nw_head


nw = node(1)
nw.next = node(2)
nw.next.next = node(4)
nw.next.next.next = node(5)
nw.next = None

temp = rotateList(nw,2)

while(temp!= None):
	print(temp.data)
	temp = temp.next



