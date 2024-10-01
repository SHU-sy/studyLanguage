import sys
n = int(sys.stdin.readline().strip())
num = list(map(int, sys.stdin.readline().split()))
s = []

for i in range(1, n+1):
    s.insert(len(s) - num[i-1], i)

print(" ".join(map(str, s)))