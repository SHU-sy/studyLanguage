import sys
n, x= map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
t = []
for i in range(n):
    if a[i]<x:
        t.append(a[i])
print(" ".join(map(str, t)))