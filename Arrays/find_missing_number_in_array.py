t = int(input())
m = 0
while(m < t):
    n = int(input())
    arr = list(map(int, input().strip().split(" ")))
    arr.append(0)
    i = 0
    while(i < n):
        if arr[i] <= 0:
            i += 1
            continue
        ele = arr[i] - 1
        if arr[ele] > 0:
            arr[i] = arr[ele]
            arr[ele] = -1
        else:
            arr[ele] -= 1
            arr[i] = 0
            i += 1
    # print(arr)
    for i in range(n):
        if arr[i] >= 0:
            print(i + 1)
            break
    m += 1
