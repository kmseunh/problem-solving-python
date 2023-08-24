def dp(x):
    MOD = 1000000000

    d = [[0] * 10 for _ in range(x + 1)]

    for i in range(1, 10):
        d[1][i] = 1

    for i in range(2, x + 1):
        for j in range(10):
            if j == 0:
                d[i][j] = d[i - 1][1]
            elif j == 9:
                d[i][j] = d[i - 1][8]
            else:
                d[i][j] = d[i - 1][j - 1] + d[i - 1][j + 1]

    return sum(d[x]) % MOD


N = int(input())
result = dp(N)
print(result)
