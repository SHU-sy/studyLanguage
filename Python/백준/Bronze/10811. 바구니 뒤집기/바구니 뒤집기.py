import sys

n, m = map(int, sys.stdin.readline().split())

b = [i for i in range(1, n+1)]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    b[i-1:j] = b[i-1:j][::-1]
print(" ".join(map(str, b)))