import sys
n, m = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
b = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
c = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        c[i][j] = a[i][j] + b[i][j]
    print(' '.join(map(str, c[i])))