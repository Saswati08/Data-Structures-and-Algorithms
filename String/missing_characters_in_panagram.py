
"""
input - 
@s = given string 

output - 
return -1 or required ans
"""
def missingPanagram(s):
    # print(ord('A'), ord('a'))
    hash_map = [0] * 26
    for i in range(len(s)):
        if s[i] >= 'A' and s[i] <= 'Z':
            hash_map[ord(s[i]) - 65] = 1
        elif s[i] >= 'a' and s[i] <='z':
            hash_map[ord(s[i]) - 97] = 1
    res = ""
    for i in range(len(hash_map)):
        if hash_map[i] == 0:
            res += chr(i + 97)
    if len(res) == 0:
        return -1
    return res


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(missingPanagram(s))
        t = t-1

# } Driver Code Ends
