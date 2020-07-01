def print_set(S, p, strs, ind, l):
    if p == l :
        strs.append(S)
    
    else:
        print_set(S, p + 1, strs, ind + 1, l)
        cpy = ""
        for i in range(0, ind):
            cpy += S[i]
        for i in range(ind + 1, len(S)):
            cpy += S[i]
        print_set(cpy, p + 1, strs, ind, l )
        
        
def powerSet(s):
    '''
    :param s: given string s
    :return: list containing power set of s.
    '''
    strs = []
    print_set(s, 0, strs, 0, len(s))
    strs = sorted(strs)
    return strs
