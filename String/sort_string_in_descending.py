t = int(input())
m = 0
while(m < t):
    string = input().strip()
    hash_map = {}
    for i in string:
        if ord(i) not in hash_map:
            hash_map[ord(i)] = 0
        hash_map[ord(i)] += 1
    i = 97 + 25
    while(i >= 97):
        if i in hash_map:
            while(hash_map[i] != 0):
                print(chr(i), end = "")
                hash_map[i] -= 1
        i -= 1
    print()
    m += 1
