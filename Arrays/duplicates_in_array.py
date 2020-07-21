def duplicates(arr, n):
	for i in range(n):
	    arr[arr[i] % n] += n
	dup_arr = []
	for i in range(n):
	    if arr[i] >= 2 * n:
	        dup_arr.append(i)
	if len(dup_arr) == 0:
	    return [-1]
	return dup_arr



#{ 
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()

