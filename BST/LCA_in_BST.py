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

def LCA(root, n1, n2):
    #code here.
    if root == None:
        return
    if root.data > n1 and root.data < n2:
        return root
    
    if root.data < n1 and root.data > n2:
        return root
        
    if root.data == n1 or root.data == n2:
        return root
        
    if n1 < root.data and n2 < root.data:
        return LCA(root.left, n1, n2)
        
    if n1 > root.data and n2 > root.data:
        return LCA(root.right, n1, n2)

if __name__ == '__main__':

	root = None
	keys = [15, 10, 20, 8, 12, 16]

	for key in keys:
		root = insert(root, key)

	print(LCA(root, 10, 16))

