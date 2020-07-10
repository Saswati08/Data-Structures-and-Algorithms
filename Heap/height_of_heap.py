import math
t = int(input())
m = 0
while(m < t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print(int(math.log(n, 2)))
    m += 1
