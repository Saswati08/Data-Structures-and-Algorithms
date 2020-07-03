class node:
    def __init__(self, val):
        self.data = val
        self.next = None

def intersectPoint(head_a,head_b):
    #code here
    c_a = 0
    curr_a = head_a
    curr_b = head_b
    while(curr_a != None):
        curr_a = curr_a.next
        c_a += 1
    c_b = 0   
    while(curr_b != None):
        curr_b = curr_b.next
        c_b += 1
    curr_a = head_a 
    curr_b = head_b
    while(c_b < c_a):
        curr_a = curr_a.next
        c_b += 1
        
    
    while(c_a < c_b):
        curr_b = curr_b.next
        c_a += 1
    
    # print(c_a, c_b, abs(c_a - c_b))
    
    # print(curr_a.data, curr_b.data)
    while(curr_a != curr_b and curr_a != None and curr_b != None):
        curr_a = curr_a.next
        curr_b = curr_b.next
        
    if curr_a == None or curr_b == None:
        return -1
        
    return curr_a.data
    

nw = node(1)
nw.next = node(2)
nw.next.next = node(4)
temp = nw.next.next
nw.next.next.next = node(5)
nw.next = None


nw2 = node(10)
nw2.next = node(20)
nw2.next = temp

print(intersectPoint(nw, nw2))
