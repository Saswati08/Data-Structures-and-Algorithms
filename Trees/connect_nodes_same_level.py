class Node: 
      
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None

def connect(root):
    '''
    :param root: root of the given tree
    :return: none, just connect accordingly.
    {
        # Node Class:
        class Node:
            def __init__(self,val):
                self.data = val
                self.left = None
                self.right = None
                self.nextRight = None
    }
    '''
    if root == None:
        return
    queue = []
    queue.append(root)
    while(len(queue) != 0):
        count = len(queue)
        i = 0
        
        d = None
        while(i < count):
            front = queue[0]
            if d:
                d.nextRight = front
            
            if front.left:
                queue.append(front.left)
            if front.right:
                queue.append(front.right)
            d = front  
            i += 1
            queue.pop(0)
        d.nextRight = None
   

root = Node(5) 
root.left = Node(2) 
root.right = Node(6) 
root.left.left = Node(1) 
root.left.right = Node(4) 
root.left.right.left = Node(3) 
root.right.right = Node(8) 
root.right.right.right = Node(9) 
root.right.right.left = Node(7)
connect(root)
