def deleteMid(s, sizeOfStack, current):
    ##Your code here
    if sizeOfStack == current or sizeOfStack == current + 1:
        s.pop(-1)
        return s
    x = s.pop(-1)
    s = deleteMid(s, len(s), current + 1)
    s.append(x)
    return s
        
s = deleteMid([1, 2, 3, 4, 5], 5, 0)
while(s):
    print(s.pop(-1))
