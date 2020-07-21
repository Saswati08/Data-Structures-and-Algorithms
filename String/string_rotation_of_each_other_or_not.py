t = int(input())
m = 0
while(m < t):
    string1 = input().strip()
    string2 = input().strip()
    l1 = len(string1)
    l2 = len(string2)
    nw = ""
    if l1 != l2:
        print(0)
    elif string1 == string2:
        print(1)
    else:
        flag = 0
        for i in range(1, l1):
            nw = string1[i:] + string1[:i]
            if nw == string2:
                flag = 1
                break
        print(flag)
            
    m += 1
