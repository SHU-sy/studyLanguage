import sys

n, m = map(int, sys.stdin.readline().split())
b=[0]*n
for i in range(n):
    b[i] = i+1

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    b[i-1], b[j-1] = b[j-1], b[i-1]

print(" ".join(map(str, b)))