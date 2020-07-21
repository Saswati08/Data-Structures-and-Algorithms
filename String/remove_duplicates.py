t = int(input())
m = 0
while(m < t):
    st = input().strip()
    hash_map = [0] * 256
    for i in range(len(st)):
        if hash_map[ord(st[i])] == 0:
            print(st[i], end = "")
            hash_map[ord(st[i])] = 1
    print()
    m += 1
