def removePair(s):
    # code here
    temp = ""
    # print(s)
    x = -1
    
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            # print("condition")
            
            temp += s[i]
            if i == len(s) - 2:
                temp += s[len(s) - 1]
            
        else:
            x = i
            break
    if x != -1:
        temp += s[i + 2 :]
        
    if len(s) == 1:
        temp = s[0]
    if len(temp) == len(s):
        # print("here")
        # print(temp, s, "lala")
        return temp
    
    else:
        # print(temp)
        temp = removePair(temp)
        if len(temp) == 0:
            temp = "Empty String"
        return temp

print(removePair("baabc"))
