N = int(input())
n = 2 * N

for i in range(1, N + 1):
    print(" " * (N - i) + "*" * ((2 * i) - 1))
