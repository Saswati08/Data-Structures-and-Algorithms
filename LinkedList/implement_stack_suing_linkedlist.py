class StackNode:

	# Constructor to initialize a node
	def __init__(self, data):
		self.data = data
		self.next = None


class Stack:

    # The method push to push element into
    # the stack
    def __init__(self):
        self.head = None
    def push(self, data):
        nw = StackNode(data)
        if self.head == None:
            self.head = nw
        else:
            nw.next = self.head
            self.head = nw
            
        # Add code here

        # The method pop which return the element
        # poped out of the stack
        

    def pop(self):
        if self.head == None:
            return -1
        x = self.head.data
        self.head = self.head.next
        return x


s = Stack()
s.push(1)
print(s.pop())
s.push(2)
s.push(3)
print(s.pop())
