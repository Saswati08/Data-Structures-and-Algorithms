t = int(input())
m = 0
while(m < t):
    string = input().strip()
    hash_map = {}
    flag = 0
    for i in range(len(string)):
        if string[i] in hash_map:
            print(string[i])
            flag = 1
            break
        hash_map[string[i]] = 1
    if flag == 0:
        print(-1)
    m += 1
