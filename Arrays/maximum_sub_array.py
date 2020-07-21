t = int(input())
m = 0
while(m < t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    max_sum = 0
    s = 0
    s_list = []
    
    for i in range(n):
        if arr[i] < 0:
            s = 0
            s_list = []
            continue
        s = s + arr[i]
        s_list.append(arr[i])
        # print(s_list)
        
        
        if max_sum <= s:
            max_sum = s
            max_sum_list = []
            for j in s_list:
                max_sum_list.append(j)
        
    # print(max_sum)
    for j in max_sum_list:
        print(j, end = " ")
    print()
    m += 1
