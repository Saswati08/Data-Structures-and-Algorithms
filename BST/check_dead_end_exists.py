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

def find_nodes_and_leaves(root, nodes, leaves):
    if root == None:
        return
    if root.left == None and root.right == None:
        leaves[root.data] = 1
        
    nodes[root.data] = 1
    find_nodes_and_leaves(root.left, nodes, leaves)
    find_nodes_and_leaves(root.right, nodes, leaves)
def isdeadEnd(root):
    # Code here
    nodes = {}
    leaves = {}
    find_nodes_and_leaves(root, nodes, leaves)
    for keys in leaves:
        if keys == 1 and keys + 1 in nodes:
            return True
        if keys - 1 in nodes and keys + 1 in nodes:
            return True
            
    return False

if __name__ == '__main__':

	root = None
	keys = [15, 10, 20, 8, 12, 16]

	for key in keys:
		root = insert(root, key)

	print(isdeadEnd(root))

