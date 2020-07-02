# Given a linked list, reverse alternate nodes and append at the end 
# Given a linked list, you have to perform the following task:

# Extract the alternative nodes from starting from second node.
# Reverse the extracted list.
# Append the extracted list at the end of the original list.
class node:
    def __init__(self, val):
        self.data = val
        self.next = None


def rearrange(head):
    # Code here
    if head.next == None:
        return head
        
    first = head
    hd1 = first
    second = head.next
    hd2 = second
    while(first != None and first.next != None):
        trail = first
        first.next = first.next.next
        first = first.next
        if second.next:
            second.next = second.next.next
            second = second.next
        
        
        
    p = hd2
    q = hd2.next
    if q:
        r = hd2.next.next
    temp = hd1
    # while(temp != None):
    #     print(temp.data, end = " ")
    #     temp = temp.next
    # print()
        
    # temp = hd2 
    # while(temp != None):
    #     print(temp.data,end =  " ")
    #     temp = temp.next
        
    # print()
    while(q != None):
        q.next = p
        p = q
        q = r
        if r:
            r = r.next
            
    hd2.next = None
    if first:
        first.next = p
    else:
        trail.next = p


nw = node(1)
nw.next = node(2)
nw.next.next = node(4)
nw.next.next.next = node(5)
nw.next = None
rearrange(nw)
temp = nw
while(temp!= None):
	print(temp.data)
	temp = temp.next
