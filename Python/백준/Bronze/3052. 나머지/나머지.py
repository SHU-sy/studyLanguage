import sys

a = [0] * 10
t = 1
for i in range(10):
    n = int(sys.stdin.readline().strip())
    a[i] = n%42

a. sort()
for i in range(9):
    if a[i] != a[i+1]:
        t += 1

print(t)