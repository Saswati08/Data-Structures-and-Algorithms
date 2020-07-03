class Node: 
    '''Structure of linked list node'''
  
    def __init__(self, data): 
        self.data = data 
        self.next = None
        self.arb = None

def copyList(head):
    '''
    param: head:  head of linkedList to copy
    return: the head of the copied linked list the #output will be 1 if successfully copied
    '''
    curr = head
    while(curr != None):
       nw = Node(curr.data)
       nw.arb = curr
       nw.next = curr.next
       curr.next = nw
       
       curr = curr.next.next
    
    curr = head.next
    while(curr != None):
        if curr.arb.arb:
            curr.arb = curr.arb.arb.next
        else:
            curr.arb = None
        if curr.next:
            curr = curr.next.next
        else:
            curr = None
        
    curr = head.next
    clone_head = head.next
    prev = head
    while(curr != None and prev != None):
        prev.next = prev.next.next
        prev = prev.next
        if curr.next:
            curr.next = curr.next.next
        curr = curr.next 
        
        
    curr = clone_head
    # while(curr != None):
    #     print(curr.data, end = " ")
    #     if curr.arb:
    #         print(curr.arb.data, end = " ")
    #     print()
    #     curr = curr.next
        
    # curr = head
    # while(curr != None):
    #     print(curr.data, end = " ")
    #     if curr.arb:
    #         print(curr.arb.data, end = " ")
    #     print()
    #     curr = curr.next
        
    return clone_head

def print_dlist(root): 
    '''Function to print the doubly linked list'''
  
    curr = root 
    while curr != None: 
        print('Data =', curr.data, ', Random =', curr.random.data) 
        curr = curr.next

original_list = Node(1) 
original_list.next = Node(2) 
original_list.next.next = Node(3) 
original_list.next.next.next = Node(4) 
original_list.next.next.next.next = Node(5) 
  
'''Set the random pointers'''
  
# 1's random points to 3 
original_list.arb = original_list.next.next
  
# 2's random points to 1 
original_list.next.arb = original_list 
  
# 3's random points to 5 
original_list.next.next.arb = original_list.next.next.next.next
  
# 4's random points to 5 
original_list.next.next.next.arb = original_list.next.next.next.next
  
# 5's random points to 2 
original_list.next.next.next.next.arb = original_list.next


cloned_list = copyList(original_list)

print('Original list:') 
print_dlist(original_list) 
print('\nCloned list:') 
print_dlist(cloned_list) 

