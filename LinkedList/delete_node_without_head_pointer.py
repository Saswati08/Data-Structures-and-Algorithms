class node:
    def __init__(self, val):
        self.data = val
        self.next = None


def deleteNode(curr_node):
    #code here
    if curr_node.next:
        curr_node.data = curr_node.next.data
        curr_node.next = curr_node.next.next
    else:
        curr_node = None
    

nw = node(1)
nw.next = node(2)
nw.next.next = node(4)
nw.next.next.next = node(5)
nw.next = None

hd = deleteNode(nw.next)
temp = hd

while(temp!= None):
	print(temp.data)
	temp = temp.next


