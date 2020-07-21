

'''
	Your task is to return the lexicographically smallest 
	max occuring charcter in given string.
	
	Function Arguments: s (given string)
	Return Type: char or -1.
	
'''

def getMaxOccurringChar(s):
    #code here
    hash_map = {}
    maxm = float('-inf')
    max_key = ''
    for i in range(len(s)):
        if s[i] not in hash_map:
            hash_map[s[i]] = 1
        else:
            hash_map[s[i]] += 1
        if maxm < hash_map[s[i]]:
            maxm = hash_map[s[i]]
            max_key = s[i]
        if maxm == hash_map[s[i]]:
            if s[i] < max_key:
                max_key = s[i]
    return max_key

