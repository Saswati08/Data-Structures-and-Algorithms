class Node: 
      
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None

class Height:
    def __init__(self):
        self.height = 0
def check(root, height):
    if root == None:
        return True
    lh = Height()
    rh = Height()
    
    
    if check(root.left, lh) and check(root.right, rh) and abs(lh.height - rh.height) <= 1:
        height.height = max(lh.height, rh.height) + 1
        return True
    else:
        height.height = max(lh.height, rh.height) + 1
        return False
def isBalanced(root):   
    #add code here
    h = Height()
    return check(root, h)
    
root = Node(5) 
root.left = Node(2) 
root.right = Node(6) 
root.left.left = Node(1) 
root.left.right = Node(4) 
root.left.right.left = Node(3) 
root.right.right = Node(8) 
root.right.right.right = Node(9) 
root.right.right.left = Node(7) 
print(isbalanced(root))
