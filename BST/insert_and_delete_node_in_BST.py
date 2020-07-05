class Node:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right
def inorder(root):

	if root is None:
		return

	inorder(root.left)
	print(root.data, end=' ')
	inorder(root.right)

def insert(root, key):

	# if the root is None, create a node and return it
	if root is None:
		return Node(key)

	# if given key is less than the root node, recur for left subtree
	if key < root.data:
		root.left = insert(root.left, key)

	# if given key is more than the root node, recur for right subtree
	else:
		root.right = insert(root.right, key)

	return root


def minm(root):
    if root.left == None:
        return root
        
    return minm(root.left)
def deleteNode(root, X):
    # code here.
    if root == None:
        return None
        
    if X < root.data:
        root.left = deleteNode(root.left, X)
        
    elif X > root.data:
        root.right = deleteNode(root.right, X)
        
    else:
        
        if root.left == None:
            temp = root.right
            return temp
            
        if root.right == None:
            temp = root.left
            return temp
            
        else:
            succ = minm(root.right)
            
            root.right = deleteNode(root.right, succ.data)
            
            root.data = succ.data
    
    return root

if __name__ == '__main__':

	root = None
	keys = [15, 10, 20, 8, 12, 16]

	for key in keys:
		root = insert(root, key)

	root = deleteNode(root, 16)
	inorder(root)

