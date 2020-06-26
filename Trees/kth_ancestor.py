class Node: 
      
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None

def kth(root, node):
    #code here
    if root == None:
        return None
    if root.data == node or kth(root.left,  node) or kth(root.right, node):
        if kth.k > 0:
            kth.k -= 1
        elif kth.k == 0:
            kth.ancs = root.data
            return None
        return root
    
    
def kthAncestor(root,k, node):
    if root.data == node and k >= 1:
        return -1
    kth.k = k
    kth.ancs = -1
    x = kth(root, node)
    return kth.ancs.data

root = Node(5) 
root.left = Node(2) 
root.right = Node(6) 
root.left.left = Node(1) 
root.left.right = Node(4) 
root.left.right.left = Node(3) 
root.right.right = Node(8) 
root.right.right.right = Node(9) 
root.right.right.left = Node(7) 
print(kthAncestor(root, 3, 9))
