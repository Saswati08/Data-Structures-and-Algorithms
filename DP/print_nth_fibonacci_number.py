
#Given a number N, print the first N Fibonacci numbers.
def printFibb(n):
    # your code here
    result = []
    
    result.append(1)
    result.append(1)
    if n == 1:
        
        return result[:1]
    if n == 2:
        return result[:2]
    else:
        for i in range(2, n):
            result.append(result[i - 1] + result[i - 2])
        return result

print(printFibb(100))
