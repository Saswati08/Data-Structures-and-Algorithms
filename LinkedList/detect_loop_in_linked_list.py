class node:
    def __init__(self, val):
        self.data = val
        self.next = None

def detectLoop(head):
    #code here
    if head == None:
        return False
    if head.next == None:
        return False
    slow = head
    fast = head.next
    while(fast != None and fast.next != None):
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    
    return False

nw = node(1)
nw.next = node(2)
nw.next.next = node(4)
nw.next.next.next = node(5)
nw.next = None

print(detecLoop(nw))
