class Node: 
      
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None

def countLeaves(root):
    # Code here
    if root == None:
        return 0
    elif root.left == None and root.right == None:
        return 1
    else :
        return countLeaves(root.left) + countLeaves(root.right)

root = Node(5) 
root.left = Node(2) 
root.right = Node(6) 
root.left.left = Node(1) 
root.left.right = Node(4) 
root.left.right.left = Node(3) 
root.right.right = Node(8) 
root.right.right.right = Node(9) 
root.right.right.left = Node(7) 
print(countLeaves(root))
