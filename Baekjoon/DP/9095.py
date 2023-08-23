def dp(x):
    if x <= 3:
        return [0, 1, 2, 4][x]

    d = [0] * (x + 1)
    d[1], d[2], d[3] = 1, 2, 4

    for i in range(4, x + 1):
        d[i] = d[i - 1] + d[i - 2] + d[i - 3]

    return d[x]


T = int(input())

for _ in range(T):
    n = int(input())
    result = dp(n)
    print(result)
