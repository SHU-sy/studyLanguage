import sys

n = int(sys.stdin.readline())
a = list(map(float, sys.stdin.readline().split()))
m = max(a)

for i in range(n):
    a[i] = a[i]/m*100
print(sum(a)/len(a))