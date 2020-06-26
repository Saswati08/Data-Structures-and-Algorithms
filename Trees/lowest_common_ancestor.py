class Node: 
      
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None

def lca(root, n1, n2):
    # Code here
    if root == None:
        return None
    if root.data == n1 or root.data == n2:
        return root
    
    # la = Node()
    # ra = Node()
    la = lca(root.left, n1, n2)
    ra = lca(root.right, n1, n2)
    
    if la != None and ra != None:
        return root
    elif la != None:
        return la
    else:
        return ra
    
root = Node(5) 
root.left = Node(2) 
root.right = Node(6) 
root.left.left = Node(1) 
root.left.right = Node(4) 
root.left.right.left = Node(3) 
root.right.right = Node(8) 
root.right.right.right = Node(9) 
root.right.right.left = Node(7) 
print(lca(root, 6, 2))
