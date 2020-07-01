def josephus(n,k):
    #Your code here
    if n == 1:
        return 1
    else:
        return ((josephus(n - 1, k) + k - 1 ) % n + 1)

josephus(5, 3)
