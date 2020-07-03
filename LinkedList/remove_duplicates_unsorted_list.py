class node:
    def __init__(self, val):
        self.data = val
        self.next = None


def removeDuplicates(head):
    # code here
    # return head after editing list
    if head.next == None:
        return head
    hash_map = {}
    prev = head
    curr = head.next
    hash_map[prev.data] = 1
    while(curr != None):
        if curr.data not in hash_map:
            hash_map[curr.data] = 1
            prev = curr
        else:
            prev.next = curr.next
            
        
        curr = curr.next
        
    return head

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

