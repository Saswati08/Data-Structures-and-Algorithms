def num_steps(i, j, m, n):
    if i == m - 1 and j == n - 1:
        return 1
    else:
        if i == m - 1:
            return (num_steps(i, j + 1, m, n))
        elif j == n - 1:
            return(num_steps(i + 1, j, m, n))
        else:
            return(num_steps(i + 1, j , m, n) + num_steps(i, j + 1, m, n))
t = int(input())
for i in range(t):
    m, n = map(int, input().split())
    c = num_steps(0, 0, m, n)
    print(c)
