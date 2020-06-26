class Node: 
      
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None

def getsum(root, level):
    if root == None:
        return
    else:
        getsum.s += root.data * level
        getsum(root.left, level * -1)
        getsum(root.right, level * -1)
def getLevelDiff(root):
    # Code here
    getsum.s = 0
    getsum(root, 1)
    return getsum.s



root = Node(5) 
root.left = Node(2) 
root.right = Node(6) 
root.left.left = Node(1) 
root.left.right = Node(4) 
root.left.right.left = Node(3) 
root.right.right = Node(8) 
root.right.right.right = Node(9) 
root.right.right.left = Node(7) 
print(getLevelDiff(root))
