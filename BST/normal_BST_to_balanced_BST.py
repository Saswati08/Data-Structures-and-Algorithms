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
def inorder(root, inorder_arr):
    if root == None:
        return
    inorder(root.left, inorder_arr)
    inorder_arr.append(root.data)
    inorder(root.right, inorder_arr)
    
def construct_tree(inorder_arr, index):
    if index[0] > index[1]:
        return None
    mid = (index[0] + index[1])//2
    key = inorder_arr[mid]
    nw = Node(key)
    nw.left = construct_tree(inorder_arr, [index[0], mid - 1])
    nw.right = construct_tree(inorder_arr, [mid + 1, index[1]])
    return nw
def buildBalancedTree(root): 
    #function should return root of the modified BST
    inorder_arr = []
    inorder(root, inorder_arr)
    # print(inorder_arr)
    index = [0, len(inorder_arr) - 1]
    return construct_tree(inorder_arr, index)
def inorder_print(root):

	if root is None:
		return

	inorder(root.left)
	print(root.data, end=' ')
	inorder(root.right)


if __name__ == '__main__':

	root = None
	keys = [15, 10, 20, 8, 12, 16]

	for key in keys:
		root = insert(root, key)

	root = buildBalancedTree(root)
	inorder_print(root)
