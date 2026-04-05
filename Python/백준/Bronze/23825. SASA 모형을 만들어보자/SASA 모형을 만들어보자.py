s, a = map(int, input().split())
s = s//2
a = a//2

if s>0 and a>0:
    print(min(s, a))
else:
    print(0)