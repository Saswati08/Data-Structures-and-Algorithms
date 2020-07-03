class node:
    def __init__(self, val):
        self.data = val
        self.next = None


def removeLoop(head):
    # code here
    # remove the loop without losing any nodes
    slow = head
    fast = head.next
    while(slow != fast and fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next
    if fast == None or fast.next == None:
        return
    curr = slow.next
    k = 1
    while(curr != slow):
        k += 1
        curr = curr.next
        
    c = 0
    curr = head
    start = head
    while(c < k):
        curr = curr.next
        c += 1
        
    
    while(start != curr):
        start = start.next
        curr = curr.next

nw = node(1)
nw.next = node(2)
nw.next.next = node(4)
nw.next.next.next = nw.next


hd = removeLoop(nw)
temp = hd

while(temp!= None):
	print(temp.data)
	temp = temp.next

        
    
    while(curr.next != start):
        curr = curr.next 
        
    curr.next = None
    return

