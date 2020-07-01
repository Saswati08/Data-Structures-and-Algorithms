def toString(List): 
    return ''.join(List) 
def permute(s, l, r):
    if l == r:
        # print(toString(s), end = " ")
        out.append(toString(s))
        return
    
    for j in range(l, r + 1):
        s[l], s[j] = s[j], s[l]
        permute(s, l + 1, r)
        s[j], s[l] = s[l], s[j]
        
        

t = int(input())
for i in range(t):
    s = list(input())
    out = []
    permute(s, 0, len(s) - 1)
    out.sort()
    for j in out:
        print(j, end = " ")
    print()
