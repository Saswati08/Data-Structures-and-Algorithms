class Node:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

def deleteNode(root, x):
    if root == None:
        return
    if x > root.data:
        root.right = deleteNode(root.right, x)
        return root
        
    else:
        if x < root.data:
            root.left = deleteNode(root.left, x)
            return root.left
            
        else:
            return root.left
            
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
if __name__ == '__main__':

	root = None
	keys = [15, 10, 20, 8, 12, 16]

	for key in keys:
		root = insert(root, key)

	root = deleteNode(root, 16)
	inorder(root)

