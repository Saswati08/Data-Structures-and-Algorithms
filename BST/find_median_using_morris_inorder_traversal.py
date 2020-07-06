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

def count_nodes(root): 
    if root == None :
        return 0
    current = root
    count = 0
    while(current != None):
        if current.left == None:
            count += 1
            current = current.right
            
        else:
            pred = current.left
            while(pred.right != None and pred.right != current):
                pred = pred.right
            if pred.right == None:
                pred.right = current
                current = current.left
            else:
                pred.right = None
                count += 1
                current = current.right
    return count
                
def findMedian(root):
    # code here
    # return the median
    # print(int(3.0))
    count = count_nodes(root)
    current = root
    currcount = 0
    while(current != None):
        if current.left == None:
            currcount += 1
            if count % 2 != 0 and currcount == count//2 + 1:
                return current.data
                
            elif count %2 == 0 and currcount == count//2 + 1:
                if (prev.data + current.data) % 2 == 0:
                    return int((prev.data + current.data)/2)
                return (prev.data + current.data)/2
                
            prev = current
            current = current.right
            
        else:
            pre = current.left
            while(pre.right != None and pre.right != current):
                pre = pre.right
                
            if pre.right == None:
                pre.right = current
                current = current.left
                
            else:
                pre.right = None
                currcount += 1
                if count % 2 != 0 and currcount == count//2 + 1:
                    return current.data
                
                elif count %2 == 0 and currcount == count//2 + 1:
                    if (prev.data + current.data) % 2 == 0:
                        return int((prev.data + current.data)/2)
                    return (prev.data + current.data)/2
                prev = current
                current = current.right

if __name__ == '__main__':

	root = None
	keys = [15, 10, 20, 8, 12, 16]

	for key in keys:
		root = insert(root, key)

	print(findMedian(root))
	


