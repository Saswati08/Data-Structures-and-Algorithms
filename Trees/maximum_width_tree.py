class Node: 
      
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None


def getMaxWidth(root):
    '''
    :param root: root of given tree.
    :return: return the Max width of the tree
    '''
    if root is None:
        return 0
    #code here
    queue = []
    maxwidth = 0
    queue.append(root)
    while(len(queue) > 0):
        
        count = len(queue)
        maxwidth = max(count, maxwidth)
        while(count > 0):
            count -= 1
            front = queue[0]
            print(front.data)    
            queue.pop()
            if front.left != None:
                queue.append(front.left)
            if front.right != None:
                queue.append(front.right)
            
    
    return maxwidth

root = Node(5) 
root.left = Node(2) 
root.right = Node(6) 
root.left.left = Node(1) 
root.left.right = Node(4) 
root.left.right.left = Node(3) 
root.right.right = Node(8) 
root.right.right.right = Node(9) 
root.right.right.left = Node(7) 
print(getMaxWidth(root))
