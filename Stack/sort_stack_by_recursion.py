def insert(x, s):
    if len(s) == 0 or s[-1] > x:
        s.append(x)
    else:
        y = s.pop(-1)
        insert(x, s)
        s.append(y)

def sorted(s):
    # Code here

    if len(s) != 0:
        temp = s.pop(-1)
        sorted(s)
        insert(temp, s)
        
    return s
    
    
print(sorted[30, 11, 1, 2, 40])
