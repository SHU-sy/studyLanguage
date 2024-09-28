import sys

n, m = map(int, sys.stdin.readline().split())
b = [0] * n

for a in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    for c in range(i-1, j):
        b[c] = k
print(" ".join(map(str, b)))