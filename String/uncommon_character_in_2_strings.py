t = int(input())
m = 0
while(m < t):
    string1 = input()
    string2 = input()
    hash_map1 = {}
    hash_map2 = {}
    # print(string1[0])
    for i in range(len(string1)):
        hash_map1[string1[i]] = 1
    for i in range(len(string2)):
        hash_map2[string2[i]] = 1
    # print(hash_map1, hash_map2)
    res = ""
    for keys in hash_map1:
        if keys not in hash_map2:
            res += keys
    for keys in hash_map2:
        if keys not in hash_map1:
            res += keys
    res = sorted(res)
    for i in res:
        print(i, end = "")
    print()
    
    m += 1
