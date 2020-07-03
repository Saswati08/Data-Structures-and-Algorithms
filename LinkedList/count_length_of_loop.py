class node:
    def __init__(self, val):
        self.data = val
        self.next = None

def countNodesinLoop(head):
    #Your code here
    if head.next == None:
        return 0
    slow = head
    fast = head.next.next
    while(fast != None and fast.next != None and slow != fast):
        slow = slow.next
        fast = fast.next.next
        
    if fast == None or fast.next == None:
        return 0
    
    temp = slow.next
    c = 1
    while(slow != temp):
        c += 1
        temp = temp.next
    return c

nw = node(1)
nw.next = node(2)
nw.next.next = node(4)
nw.next.next.next = nw
#nw.next = None

print(countNodesinLoop(nw))
