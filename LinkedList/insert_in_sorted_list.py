class node:
    def __init__(self, val):
        self.data = val
        self.next = None


def  insertInSorted(head,data):
    #code here
    if head == None:
        return
    if data < head.data:
        nw = Node(data)
        nw.next = head
        return nw
   
    prev = head
    curr = head.next
    
    
    
    while(prev != None):
        if  curr == None or curr.data > data :
            nw = Node(data)
            prev.next = nw
            nw.next = curr
            break
        prev = curr
        curr = curr.next
        
    return head

nw = node(1)
nw.next = node(2)
nw.next.next = node(4)
nw.next.next.next = node(5)
nw.next = None

hd = insertInSorted(nw, 3)
temp = hd

while(temp!= None):
	print(temp.data)
	temp = temp.next


