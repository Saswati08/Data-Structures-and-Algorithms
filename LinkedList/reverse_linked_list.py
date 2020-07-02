class node:
    def __init__(self, val):
        self.data = val
        self.next = None


def reverseList(head):
    # Code here
    if head == None:
        return
    if head.next == None:
        return head
        
    p = head
    q = head.next
    r = q.next
    p.next = None
    while(q != None):
        q.next = p
        p = q
        q = r
        if r != None:
            r = r.next
    return p

nw = node(1)
nw.next = node(2)
nw.next.next = node(3)
nw.next.next.next = node(4)
nw.next = None

reversed_hd = reverseList(nw)
temp = reversed_hd

while(temp!= None):
	print(temp.data)
	temp = temp.next
