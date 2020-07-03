import gc 
  
# A node of the doublly linked list 
class Node: 
      
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data  
        self.next = None
        self.prev = None
  
class DoublyLinkedList: 
     # Constructor for empty Doubly Linked List 
    def __init__(self): 
        self.head = None
   
   # Function to delete a node in a Doubly Linked List. 
   # head_ref --> pointer to head node pointer. 
   # dele --> pointer to node to be deleted


def deleteNode(head, x):
    # Code here
    if x == 1:
        head = head.next
        head.prev = None
        # print(head.data, head.next.data)
        return head
        
    curr = head
    c = 1
    while(c != x and curr != None):
        curr = curr.next
        c += 1


# Given a reference to the head of a list and an 
    # integer, inserts a new node on the front of list 
    def push(self, new_data): 
   
        # 1. Allocates node 
        # 2. Put the data in it 
        new_node = Node(new_data) 
   
        # 3. Make next of new node as head and 
        # previous as None (already None) 
        new_node.next = self.head 
   
        # 4. change prev of head node to new_node 
        if self.head is not None: 
            self.head.prev = new_node 
   
        # 5. move the head to point to the new node 
        self.head = new_node 
  
  
    def printList(self, node): 
        while(node is not None): 
            print node.data, 
            node = node.next
  
  
# Driver program to test the above functions 
  
# Start with empty list 
dll = DoublyLinkedList() 
  
# Let us create the doubly linked list 10<->8<->4<->2 
dll.push(2); 
dll.push(4); 
dll.push(8); 
dll.push(10); 
  
print "\n Original Linked List", 
dll.printList(dll.head) 
  
# delete nodes from doubly linked list 
dll.deleteNode(dll.head) 
dll.deleteNode(dll.head.next) 
dll.deleteNode(dll.head.next) 
# Modified linked list will be NULL<-8->NULL 
print "\n Modified Linked List", 
dll.printList(dll.head)
        
    
