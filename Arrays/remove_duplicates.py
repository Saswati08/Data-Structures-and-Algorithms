from collections import OrderedDict
t = int(input())
m = 0
while(m < t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    res = list(OrderedDict.fromkeys(arr))
    for i in res:
        print(i, end = " ")
    print()
    m += 1
