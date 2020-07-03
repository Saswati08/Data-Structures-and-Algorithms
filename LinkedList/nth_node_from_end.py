class node:
    def __init__(self, val):
        self.data = val
        self.next = None

def getNthfromEnd(head,n):
    #code here
    slow = head
    fast = head
    c = 1
    while(c <= n and fast != None):
        fast = fast.next
        if fast == None:
            break
        c += 1
    if fast == None and c < n:
        return -1
    while(fast != None):
        fast = fast.next
        slow = slow.next
        
    return slow.data

nw = node(1)
nw.next = node(2)
nw.next.next = node(4)
nw.next.next.next = node(5)
nw.next = None

print(getNthfromEnd(nw, 3))

