class node:
    def __init__(self, val):
        self.data = val
        self.next = None

def removeDuplicates(head):
    #code here
    if head.next == None:
        return head
    prev = head
    curr = head.next
    
        
    
    while(curr != None):
        if curr.data != prev.data:
            prev.next = curr
            prev = curr
        curr = curr.next
        
    prev.next = None

nw = node(2)
nw.next = node(2)
nw.next.next = node(2)
nw.next.next.next = node(2)
nw.next = None

hd = removeDuplicates(nw)
temp = hd

while(temp!= None):
	print(temp.data)
	temp = temp.next

