class node:
    def __init__(self, val):
        self.data = val
        self.next = None
# Given a singly linked list of size N of integers. The task is to check if the given linked list is palindrome or not.
# Expected Time Complexity: O(N)
# Expected Auxialliary Space Usage: O(1)  (ie, you should not use the recursive stack space as well)
def isPalindrome(head):
    #code here
    if head == None:
        return True
    if head.next == None:
        return True
    mid = head
    fast = head.next
    while(fast != None):
        mid = mid.next
        if fast.next:
            fast = fast.next.next
        else:
            fast = fast.next

    p = mid
    q = mid.next
    if mid.next:
        r = mid.next.next
    else:
        r = mid.next
    mid.next = None
    while(q != None):
        q.next = p
        p = q
        q = r
        if r:
            r = r.next
            
    straight = head
    reverse = p
    
    while(straight != reverse and reverse != None):
        if straight.data != reverse.data:
            return False
        straight = straight.next
        reverse = reverse.next
        
    return True

nw = node(1)
nw.next = node(2)
nw.next.next = node(2)
nw.next.next.next = node(1)
nw.next = None

print(isPalindrome(nw))
    
