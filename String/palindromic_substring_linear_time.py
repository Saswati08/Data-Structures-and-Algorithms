def LongestPalindromeSubString(text):
    # code here
    # return the longest palindrome substring
    string_list = []
    string_list =  ['$']
    for i in range(len(text)):
        string_list.append('#')
        string_list.append(text[i])
    string_list.append('#')
    string_list.append('@')
    # print(string_list)
    r = 0
    c = 0
    length = [0] * len(string_list)
    maxm = 0
    maxi = -1
    for i in range(1, len(string_list) - 1):
        mirror = 2 * c  - i
        if i < r:
            length[i] = min(r- i, length[mirror])
        while(string_list[i + (length[i] + 1)] == string_list[i - (length[i] + 1)]):
            length[i] += 1
        if i > c:
            c = i
            r = i + length[i]
            
        if maxm < length[i]:
            maxm = length[i]
            maxi = i
            
    res = ""
    for i in range(maxi - maxm, maxi + maxm):
        if string_list[i] == '#' or string_list[i] == '$' or string_list[i] == '@':
            continue
        res = res + string_list[i]
    return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        text=input().strip()
        print(LongestPalindromeSubString(text))

# } Driver Code Ends
