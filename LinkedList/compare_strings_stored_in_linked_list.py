class node:
    def __init__(self, val):
        self.data = val
        self.next = None


def compare(head1, head2):
    #return 1/-1/0
    first = head1
    second = head2
    
    while(first != None and second != None):
        if first.data != second.data:
            if ord(first.data) > ord(second.data):
                return 1
            else:
                return -1
                
        first = first.next
        second = second.next
        
    if first == None and second != None:
        return -1
    if second == None and first != None:
        return 1
    
    return 0

nw = node('a')
nw.next = node('b')
nw.next.next = node('a')
nw.next.next.next = node('a')
nw.next = None

nw2 = node('a')
nw2.next = node('b')
nw2.next.next = node('b')
nw2.next.next.next = node('a')
nw2.next = None


print(compare(nw, nw2))
