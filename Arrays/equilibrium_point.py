t = int(input())
m = 0
while(m < t):
    n = int(input())
    arr = list(map(int, input().strip().split(" ")))
    tot_sum = 0
    for i in arr:
        tot_sum += i
    s = arr[0]
    flag = 1
    for i in range(1, len(arr)):
        if s == tot_sum - arr[i] - s:
            print(i + 1)
            flag = 0
            break
        s += arr[i]
    if flag and n != 1:
        print(-1)
    if n == 1:
        print(1)
    m += 1
