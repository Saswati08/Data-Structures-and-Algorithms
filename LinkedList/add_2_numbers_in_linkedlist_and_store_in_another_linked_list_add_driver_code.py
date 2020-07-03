def addLists(first, second):
    # code here
    # return head of sum list
    curr1 = first
    num1 = []
    while(curr1 != None):
        num1.append(curr1.data)
        curr1 = curr1.next
        
    num2 = []
    curr2 = second
    while(curr2 != None):
        num2.append(curr2.data)
        curr2 = curr2.next
    c = 0 
    curr = None
    while(len(num1) > 0 and len(num2) > 0):
        d1 = num1[-1]
        num1.pop(-1)
        d2 = num2[-1]
        num2.pop(-1)
        d = (d1 + d2 + c) % 10
        c = (d1 + d2 + c) //10
        nw = Node(d)
        if curr:
            curr.next = nw
        else:
            head_node = nw
            
        curr = nw
    while(len(num1) > 0):
        d = (num1[-1] + c) % 10
        c = (num1[-1] + c) //10
        nw = Node(d)
        if curr:
            curr.next = nw
        else:
            head_node = nw
        curr = nw
        num1.pop(-1)
        
    while(len(num2) > 0):
        d = (num2[-1] + c) % 10
        c = (num2[-1] + c) //10
        nw = Node(d)
        if curr:
            curr.next = nw
            
        else:
            head_node = nw
        curr = nw
        num2.pop(-1)
    if c != 0:
        nw = Node(c)
        curr.next = nw
        curr = nw
        
    
    p = head_node
    q = head_node.next
    if q == None:
        return head_node
    r = head_node.next.next
    p.next = None
    while(q != None):
        q.next = p
        p = q
        q = r
        if r:
            r = r.next
    return p
        
