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
def check_BST(root, minm, maxm):
    if root == None:
        return True
    if root.data <= minm or root.data >= maxm:
        return False
    return check_BST(root.left, minm, root.data) and check_BST(root.right, root.data, maxm)
def isBST(root):
    #code here
    maxm = float('inf')
    minm = float('-inf')
    return check_BST(root, minm, maxm)

if __name__ == '__main__':

	root = None
	keys = [15, 10, 20, 8, 12, 16]

	for key in keys:
		root = insert(root, key)

	print(isBST(root))

