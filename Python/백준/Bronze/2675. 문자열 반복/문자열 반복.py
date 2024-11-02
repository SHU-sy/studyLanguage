import sys
t = int(sys.stdin.readline().strip())
for _ in range(t):
    r, s = sys.stdin.readline().split()
    a = ""
    for i in range(len(s)):
         a += s[i] * int(r)
    print(a)