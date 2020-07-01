letters = {2:['a', 'b', 'c'], 3:['d', 'e', 'f'], 4:['g', 'h', 'i'], 5:['j', 'k', 'l'], 6:['m', 'n', 'o'], 7 : ['p', 'q', 'r', 's'], 8 :['t', 'u', 'v'], 
9:['w', 'x', 'y', 'z']}
t = int(input())
for m in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    # print(t, n, a)
    ans = letters[a[0]]
    for i in a[1:]:
        temp = []
        for j in ans:
            for k in letters[i]:
                temp.append(j + k)
        ans = temp
    for i in ans:
        print(i, end = " ")
    print()
    
