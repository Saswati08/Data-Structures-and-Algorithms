t = int(input())
m = 0
while(m < t):
    n = int(input())
    string_list = list(input().strip().split(" "))
    string_list = sorted(string_list)
    # print(string_list)
    st1 = string_list[0]
    st2 = string_list[n - 1]
    for i in range(len(st1) + 1):
        if i == len(st2) or i == len(st1):
            break
        elif st1[i] != st2[i]:
            break
    # print(i)
    if i == 0:
        print("-1")
    else:
        print(st1[:i])
    m += 1
