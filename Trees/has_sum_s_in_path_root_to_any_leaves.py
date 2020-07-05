class Node:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

def hasPathSum(root, sm):
    '''
    :param root: root of given tree.
    :param sm: root to leaf sum
    :return: true or false
    '''
    # code here
    if root == None:
        return False
    if root.left == None and root.right == None:
        if sm - root.data == 0:
            return True
        else:
            return False
            
    if hasPathSum(root.left, sm - root.data) or hasPathSum(root.right, sm - root.data):
        return True
    return False

root = Node(5) 
root.left = Node(2) 
root.right = Node(6) 
root.left.left = Node(1) 
root.left.right = Node(4) 
root.left.right.left = Node(3) 
root.right.right = Node(8) 
root.right.right.right = Node(9) 
root.right.right.left = Node(7) 
print(hasPathSum(root, 8))
