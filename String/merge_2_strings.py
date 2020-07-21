t = int(input())
m = 0
while(m < t):
    string1, string2 = input().strip().split()
    i = 0
    j = 0
    itr = 1
    while(i < len(string1) and j < len(string2)):
        if itr & 1:
            print(string1[i], end = "")
            i += 1
        else:
            print(string2[j], end = "")
            j += 1
        itr += 1
    while(i < len(string1)):
        print(string1[i], end ="")
        i += 1
    while(j < len(string2)):
        print(string2[j], end = "")
        j += 1
    print()
    m += 1
