def SubsequenceLength(s):
    #Codee here
    left = 0
    right = 0
    maxm = 0
    hash_map = {}
    while right < len(s):
        if s[right] in hash_map:
            if left < hash_map[s[right]] + 1:
                left = hash_map[s[right]] + 1
            # left = max(left, hash_map[s[right]] + 1)
        
        hash_map[s[right]] = right
        if maxm < right - left + 1:
            maxm = right - left + 1
        right += 1
    return maxm
        


#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    s = input()
    print(SubsequenceLength(s))
    
# } Driver Code Ends
