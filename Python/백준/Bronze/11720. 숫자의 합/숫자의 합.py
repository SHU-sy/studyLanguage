import sys
n = int(sys.stdin.readline().strip())
w = sys.stdin.readline().strip()
s = 0
for i in range(n):
    s += int(w[i])
print(s)