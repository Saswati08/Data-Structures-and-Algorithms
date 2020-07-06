class Node:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right
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

def getCountOfNode(root,l,h):
    ##Your code here
    if root == None:
        return 0
    if root.data >= l and root.data <= h:
        return 1 + getCountOfNode(root.left, l, h) + getCountOfNode(root.right, l, h)
        
    return getCountOfNode(root.left, l, h) + getCountOfNode(root.right, l, h)

if __name__ == '__main__':

	root = None
	keys = [15, 10, 20, 8, 12, 16]

	for key in keys:
		root = insert(root, key)
	print(getCountOfNode(root, 10, 15))

