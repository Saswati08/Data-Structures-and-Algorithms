# Function should return 1/0 or True/False
def areKAnagrams(str1, str2, k):
    # Code here
    hash_map1 = {}
    hash_map2 = {}
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        if str1[i] not in hash_map1:
            hash_map1[str1[i]] = 0
        hash_map1[str1[i]] += 1
        if str2[i] not in hash_map2:
            hash_map2[str2[i]] = 0
        hash_map2[str2[i]] += 1
    
    # print(hash_map1)
    # print(hash_map2)
    for keys in hash_map1:
        
        if keys not in hash_map2:
            k -= hash_map1[keys]
            # hash_map1[str1[i]] = -1
        elif hash_map1[keys] > hash_map2[keys]:
            k -= hash_map1[keys] - hash_map2[keys]
            # hash_map1[str1[i]] = -1
        if k < 0:
            return False
    return True


#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        arr = input().strip().split()
        k = int(input())
        if areKAnagrams(arr[0], arr[1], k):
            print(1)
        else:
            print(0)
# Contributed By: Harshit sidhwa
# } Driver Code Endss
