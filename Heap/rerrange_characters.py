# Given a string S with repeated characters (only lowercase). The task is to rearrange characters in a string such that no two adjacent characters are same.

# Note : It may be assumed that the string has only lowercase English alphabets.
from heapq import heappush, heappop, heapify
t = int(input())
m = 0
while(m < t):
    h = []
    string = input().strip()
    hash_map = {}
    for i in range(len(string)):
        if string[i] not in hash_map:
            hash_map[string[i]] = 0
        hash_map[string[i]] += 1
    for keys in hash_map:
        heappush(h, (hash_map[keys] * -1, keys))
    prev = (1, '#')
    res = ""
    # print(h)
    while(h):
        freq, ch = heappop(h)
        freq *= -1
        res += ch
        if prev[0] * -1 > 0:
            heappush(h, prev)
        freq -= 1
        prev = (-freq, ch)
    # print(res)    
    if len(res) == len(string):
        print(1)
    else:
        print(0)
    m += 1
