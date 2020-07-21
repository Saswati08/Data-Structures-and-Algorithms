t = int(input())
m = 0
value = {'I' : 1, 'V' : 5, 'X': 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
while(m < t):
    st = input()
    i = 0
    res = 0
    for i in range(len(st)):
        if i == len(st) - 1:
            res += value[st[i]]
        else:
            x = value[st[i]]
            y = value[st[i + 1]]
            if x >= y:
                res += x 
            elif x < y:
                res -= x
    print(res)
    m += 1
