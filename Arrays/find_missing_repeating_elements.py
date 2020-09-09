t = int(input())
m = 0
while(m < t):
    n = int(input())
    arr = input().split()
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    # print(arr)
    # arr = list(map(int, input().strip().split(" ")))
    i = 0
    while(i < n):
        if arr[i] <= 0:
            i += 1
            continue
        else:
            ele_index = arr[i] - 1
            if arr[ele_index] > 0:
                arr[i] = arr[ele_index]
                arr[ele_index] = -1
            else:
                arr[ele_index] -= 1
                arr[i] = 0
                i += 1
    miss = -1
    repeat = -1
    for i in range(n):
        if arr[i] == -2:
            repeat = i + 1
        elif arr[i] >= 0:
            miss = i + 1
    print(repeat, miss)
            
    m += 1
