#Your function should return a String
dec = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
rom = ['I', 'IV', 'V','IX', 'X','XL','L','XC', 'C','CD', 'D','CM', 'M']

def convertRoman(n):
    #Code here
    res = ""
    ind = 12
    while(n):
        div = n // dec[ind]
        n = n % dec[ind]
        while(div):
            res += rom[ind]
            div -= 1
        ind -= 1
    return res
            


#{ 
#  Driver Code Starts
#Your Code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(convertRoman(n))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends
