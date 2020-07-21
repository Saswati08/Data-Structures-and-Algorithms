def countDistinct(arr, n, k):
    # Code here
    hash_map = {}
    res = []
    distinct_ele = 0
    for i in range(k):
        if arr[i] not in hash_map:
            hash_map[arr[i]] = 0
            distinct_ele += 1
        hash_map[arr[i]] += 1
    res.append(distinct_ele)
    for i in range(k, n):
        
        if hash_map[arr[i - k]]  == 1:
            
            distinct_ele -= 1
        hash_map[arr[i - k]] -= 1
            
        if arr[i] not in hash_map or hash_map[arr[i]] == 0:
            hash_map[arr[i]] = 0
            distinct_ele += 1
            
        hash_map[arr[i]] += 1
        res.append(distinct_ele)
        # print(res)
    return res
        
#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        res = countDistinct(arr, n, k)
        for i in res:
            print (i, end = " ")
        print ()
# } Driver Code Ends
