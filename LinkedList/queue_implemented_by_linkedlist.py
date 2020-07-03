class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class MyQueue:
    
     def __init__(self):
        self.front = None
        self.rear = None
     # Method to add an item to the queue
     def push(self, item): 
        nw = Node(item)
        if self.front == None:
            self.front = nw
            self.rear = nw
            
        self.rear.next = nw
        self.rear = nw
            
         #Add code here
    
    # Method to remove an item from queue
     def pop(self):
        if self.front == None:
            return -1
        
        x = self.front.data
        
        
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        
        return x

q = MyQueue()
q.push(1)
q.push(2)
print(q.pop())
q.push(3)
print(q.pop())
