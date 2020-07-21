'''
	Your task is to merge the given k sorted
	linked lists into one list and return
	the the new formed linked list class.

	Function Arguments:
	    arr is a list containing the n linkedlist head pointers
	    n is an integer value
    
    node class:
    
class Node:
    def __init__(self,x):
        self.data = x
        self.nxt = None
        
        
'''
from heapq import heappush, heappop, heapify
class wrapper:
    def __init__(self, node):
        self.data = node.data
        self.next = node.next
    def __lt__(self, other):
        return self.data < other.data
def mergeKLists(arr, n):
    heap = []
    for i in range(n):
        heap_obj = wrapper(arr[i])
        heappush(heap, heap_obj)
    # for i in heap:
    #     print(i.data)
    head = None
    tail = None
    
    while(heap):
        # for i in heap:
        #     print(i.data, end = " ")
        # print()
        front_obj = heappop(heap)
        
        
        if tail:
            tail.next = front_obj
        else:
            head = front_obj
        tail = front_obj
        if front_obj.next:
            # print(front.next.data)
            node = front_obj.next
            heap_obj = wrapper(node)
            heappush(heap, heap_obj)
    tail.next = None
    return head

#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def add(self,x):
        if self.head is None:
            self.head=Node(x)
            self.tail=self.head
        else:
            self.tail.next=Node(x)
            self.tail=self.tail.next
    
def printList(head):
    walk = head
    while walk:
        print(walk.data, end=' ')
        walk=walk.next
    print()

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        line=[int(x) for x in input().strip().split()]
        
        heads=[]
        index=0
        
        for i in range(n):
            size=line[index]
            index+=1
            
            newList = LinkedList()
            
            for _ in range(size):
                newList.add(line[index])
                index+=1
            
            heads.append(newList.head)
        
        merged_list = mergeKLists(heads,n)
        printList(merged_list)

# } Driver Code Ends
