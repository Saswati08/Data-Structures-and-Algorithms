class Node: 
      
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None

def vertical(root, l):
    if root == None:
        return 
    if l < vertical.minm:
        vertical.minm = l
    elif l > vertical.maxm:
        vertical.maxm = l
    vertical(root.left, l - 1)
    vertical(root.right, l + 1)

def verticalWidth(root):
    '''
    :param root: root of the given tree.
    :return: Integer
    '''
    # code here
    if root == None:
        return 0
    vertical.minm = 1000
    vertical.maxm = 0
    vertical(root, 0)
    return vertical.maxm - vertical.minm  + 1 

root = Node(5) 
root.left = Node(2) 
root.right = Node(6) 
root.left.left = Node(1) 
root.left.right = Node(4) 
root.left.right.left = Node(3) 
root.right.right = Node(8) 
root.right.right.right = Node(9) 
root.right.right.left = Node(7) 
print(verticalWidth(root))
