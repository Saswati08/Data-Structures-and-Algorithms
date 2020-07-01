#User function Template for python3
# Given a string, the task is to find whether it contains an additive sequence or not. A string contains an additive sequence if its digits can make a sequence of numbers in which every number is addition of previous two numbers. You are required to complete the function which returns true if the string is a valid sequence else returns false.
def isAdd(a, b, c):
    # print(a, b, c)
    if len(c) == 0:
        return True
    s = int(a) + int(b)
    s = str(s)
    # print(s, a, b)
    if len(s) > len(c) or s != c[0:len(s)]:
        # print(s, c[0:len(s)])
        return False
    return isAdd(b, s, c[len(s):])
    
    

def isAdditiveSequence(num):
    #code here
    
    num = num.strip()
    for i in range(1, len(num)//2 + 1):
        for j in range(1, (len(num) - i)//2 + 1):
            a, b, c = num[0:i], num[i:i +j], num[i + j:]
            # print(a, b, c)
            # if len(a) == 0 or len(b) == 0 or len(c) == 0:
            #     # print("Gadbad")
            #     continue
            
            res = isAdd(a, b, c)
            # print(res, a, b, c)
            if res == True:
                break
        if res == True:
            break
    if res == True:
        return 1
    else:
        return 0
    # return 1
