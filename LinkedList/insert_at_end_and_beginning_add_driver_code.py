# function inserts data x in front of list and returns new head 
def insertAtBegining(head,x):
    # code here 
    nw = Node(x)
    nw.next = head
    return nw

# function appends data x at the end of list and returns new head
def insertAtEnd(head,x):
    # code here 
    curr = head
    while(curr != None and curr.next != None ):
        curr = curr.next
    nw = Node(x)
    if curr:
        curr.next = nw
        return head
    else:
        return nw
