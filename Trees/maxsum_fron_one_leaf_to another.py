class Node: 
      
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None


def maxsum(root):
    if root == None:
        return 0
        
    # if root.left == None and root.right == None:
    #     return root.data
        
    ls = maxsum(root.left)
    rs = maxsum(root.right)
    if root.left != None and root.right != None:
        maxsum.s = max(ls + rs + root.data, maxsum.s)
        return max(ls, rs) + root.data
        
    if root.left is None:
        return rs + root.data
    else:
        return ls + root.data
def maxPathSum(root):
    # code here 
    maxsum.s = float('-inf')
    maxsum(root)
    return  maxsum.s

root = Node(5) 
root.left = Node(2) 
root.right = Node(6) 
root.left.left = Node(1) 
root.left.right = Node(-4) 
root.left.right.left = Node(3) 
root.right.right = Node(-8) 
root.right.right.right = Node(9) 
root.right.right.left = Node(7) 
print(maxPathSum(root))
