import sys
a = list(map(int, (sys.stdin.readline() for _ in range(9))))
print(max(a))
print(a.index(max(a))+1)