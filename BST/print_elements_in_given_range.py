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

def store_in_range_elements(root, low, high, res):
    if root == None:
        return
    store_in_range_elements(root.left, low, high, res)
    if root.data >= low and root.data <= high:
        # print(root.data, end = " ")
        res.append(root.data)
    store_in_range_elements(root.right, low, high, res)
def printNearNodes(root, low, high):
    #code here.
    res = []
    store_in_range_elements(root, low, high, res)
    return res
    
if __name__ == '__main__':

	root = None
	keys = [15, 10, 20, 8, 12, 16]

	for key in keys:
		root = insert(root, key)

	res = printNearNodes(root, 10, 16)
	print(res)

