t = int(input())
m = 0
while(m < t):
    string = input().strip()
    l = len(string)
    value = {'0' : 0, '1' : 1, '2': 2, '3' : 3, '4': 4, '5':5, '6':6, '7':7, '8':8, '9':9}
    i = 0
    maxm = 0
    while(i < l):
        res = 0
        while(i < l and string[i] >= '0' and string[i] <= '9'):
            res = res * 10 + value[string[i]]
            maxm = max(res, maxm)
            i += 1
        i += 1
    print(maxm)
    m += 1
