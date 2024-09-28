import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())
s = 0

for i in range(n):
    if a[i]==v:
        s+=1
print(s)