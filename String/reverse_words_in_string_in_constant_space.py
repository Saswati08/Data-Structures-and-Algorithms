t = int(input())
m = 0
while(m < t):
    st = input()
    l = len(st)
    st += '.'
    
    i = len(st) - 1
    while(i >= 0):
        j = i - 1
        while(j >= 0 and st[j] != '.'):
            j -= 1
        w = st[j + 1 : i + 1]
        st = st + w
        i = j
    print(st[l + 1 : -1])
    m += 1
