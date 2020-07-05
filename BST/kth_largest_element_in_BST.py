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

def cal_kth_largest(root, k, c):
    if root == None:
        return
    right = cal_kth_largest(root.right, k, c)
    if right:
        return right
        
    if c[0] == k:
        return root
    c[0] += 1
    
    left = cal_kth_largest(root.left, k, c)
    if left:
        return left
        
    return None
        
def kthLargest(root, k):
    c = []
    c.append(1)
    kth = cal_kth_largest(root, k, c)
    return kth.data


if __name__ == '__main__':

	root = None
	keys = [15, 10, 20, 8, 12, 16]

	for key in keys:
		root = insert(root, key)

	print(kthLargest(root, 3))
	#inorder(root)
