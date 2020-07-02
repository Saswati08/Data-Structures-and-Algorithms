class node:
    def __init__(self, val):
        self.data = val
        self.next = None

def pairWiseSwap(head):
    # code here
    if head.next == None:
        return head
        
    # if head.next.next == None:
    #     head.data, head.next.data = head.next.data, head.data
    #     return head
        
    # ptr = head
    first = head
    second = head.next
    while(first != None and first.next != None):
        # temp = first.data
        first.data, second.data = second.data, first.data
        # second.data = temp
        
        first = second.next
        if first:
            second = first.next
        ptr = first
        
    return head

nw = node(1)
nw.next = node(2)
nw.next.next = node(4)
nw.next.next.next = node(5)
nw.next = None

hd = pairWiseSwap(nw)
temp = hd

while(temp!= None):
	print(temp.data)
	temp = temp.next

