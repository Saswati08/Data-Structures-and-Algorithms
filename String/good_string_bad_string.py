# In this problem, a String S is composed of lowercase alphabets and wildcard characters i.e. '?'. Here, '?' can be replaced by any of the lowercase alphabets. Now you have to classify the given String on the basis of following rules:

# If there are more than 3 consonants together or more than 5 vowels together, the String is considered to be "BAD". A String is considered "GOOD" only if it is not “BAD”.
t = int(input())
m = 0
while(m < t):
    string = input()
    vowels = dict()
    vowels['a'] = 1
    vowels['e'] = 1
    vowels['i'] = 1
    vowels['o'] = 1
    vowels['u'] = 1
    v = 0
    c = 0
    flag = 1
    for i in range(len(string)):
        if string[i].isalpha():
            if string[i] in vowels:
                if c > 0:
                    c = 0
                v += 1
            else:
                if v > 0:
                    v = 0
                c += 1
            
        else:
            v += 1
            c += 1
        if v > 5 or c > 3:
            flag = 0
            break
        
    print(flag)
    m += 1
