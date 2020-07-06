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
def modify(root):
    #code here
    stack = []
    current = root
    s = 0
    while(stack or current):
        
        while(current):
            stack.append(current)
            current = current.right
            
        if stack:
            top = stack[-1]
            # print(current.data)
            top.data += s
            s = top.data
            
            stack.pop(-1)
            # if stack1:
            #     stack1.pop(-1)
            # if stack1:
            #     print(stack1[-1].data, "Still here")
            current = top.left
            
        
    # print()
    return root

if __name__ == '__main__':

	root = None
	keys = [15, 10, 20, 8, 12, 16]

	for key in keys:
		root = insert(root, key)
	root = modify(root)
	inorder(root)
