def isCircular(head):
    # Code here
    if head.next == None:
        return False
    hd_cpy = head
    curr = head.next
    while(curr != hd_cpy):
        if curr == None:
            return False
        curr = curr.next
        
    return True

