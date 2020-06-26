class Node: 
      
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None

def areMirror(root1,root2):
    '''
    :param root1,root2: two root of the given trees.
    :return: True False
    
    '''
    #code here
    if root1 == None and root2 == None:
        return True
    if root1 == None or root2 == None:
        return False
    if root1.data != root2.data :
        return False
    return areMirror(root1.left, root2.right) and areMirror(root1.right, root2.left)
root = Node(5) 
root.left = Node(2) 
root.right = Node(6) 
root.left.left = Node(1) 
root.left.right = Node(4) 
root.left.right.left = Node(3) 
root.right.right = Node(8) 
root.right.right.right = Node(9) 
root.right.right.left = Node(7) 

root2 = Node(5) 
root2.left = Node(2) 
root2.right = Node(6) 
root2.left.left = Node(1) 
root2.left.right = Node(4) 
root2.left.right.left = Node(3) 
root2.right.right = Node(8) 
root2.right.right.right = Node(9) 
root2.right.right.left = Node(7) 

print(areMirror(root, root2))
