class Node:
	def __init__(self, value): 
	self.key = value 
	self.left = None
	self.right = None



def isHeap(root):
    #Code Here
    if root.left == None and root.right == None:
        return True
        
    if root.left == None and root.right != None:
        return False
        
    if root.left and root.right:
        return root.data >= root.left.data and root.data >= root.right.data and isHeap(root.left) and isHeap(root.right)
        
    if root.left:
        return root.data >= root.left.data
        
    else:
        return False
        
        
    
root = Node(5) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(1) 
