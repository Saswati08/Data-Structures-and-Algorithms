#Given a Linked list, rearrange it such that converted list should be of the form a < b > c < d > e < f .. where a, b, c are consecutive data node of linked list and such that the order of linked list is sustained.
#For example: In 11 15 20 5 10 we consider only 11 20 5 15 10 because it satisfies the above condition and the order of linked list. 5 20 11 15 10 is not considered as it does not follow the order of linked list.

class node:
    def __init__(self, val):
        self.data = val
        self.next = None

def zigzag(head):
    # Complete this function
    flag = True
    curr = head
    while(curr and curr.next):
        if flag:
            if curr.data> curr.next.data:
                curr.data, curr.next.data = curr.next.data, curr.data
        else:
            if curr.data < curr.next.data:
                curr.data, curr.next.data = curr.next.data, curr.data
        if flag:
            flag = False
        else:
            flag = True
        curr = curr.next
    return head

nw = node(1)
nw.next = node(2)
nw.next.next = node(4)
nw.next.next.next = node(5)
nw.next = None

hd = zigzag(nw)
temp = hd

while(temp!= None):
	print(temp.data)
	temp = temp.next

