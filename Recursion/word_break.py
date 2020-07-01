#User function Template for python3
def checkwordBreak(line, dictionary, ind, a):
    if ind == len(line):
        return True
    cpy = ""
    for i in range(ind, len(line)):
        cpy += line[i]
        if cpy in dictionary:
            # print(cpy)
            a = a + " " + cpy
            # print(a)
            c = checkwordBreak(line, dictionary, i + 1, a)
            # print(c)
            if c == True :
                return True
    return False
        

def wordBreak(line, dictionary):
    # Complete this function
    a = ""
    f = checkwordBreak(line, dictionary, 0, a)
    # print(a)
    return f
