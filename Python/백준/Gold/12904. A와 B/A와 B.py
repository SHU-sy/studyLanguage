import sys
input = sys.stdin.readline

s = input().strip()
t = input().strip()
s_len = len(s)

while len(t) > s_len:
    if t[-1] == 'A':
        t = t[:-1]
    elif t[-1] == 'B':
        t = t[:-1][::-1]

if t == s:
    print(1)
else:
    print(0)
