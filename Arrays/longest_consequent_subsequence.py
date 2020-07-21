def findLongestConseqSubseq(arr, n):
    # code here
    store = dict()
    for i in range(n):
        store[arr[i]] = i
    c = 1
    result = 1
    for i in range(n):
        if arr[i] - 1 in store:
            continue
        k = arr[i] + 1
        c = 1
        while(k in store):
            c += 1
            k += 1
        result = max(result, c)
    
    return result
        



#{ 
#  Driver Code Starts
# Driver function 
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        print(findLongestConseqSubseq(arr, n[0]))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends
