import sys
input = sys.stdin.readline

x = int(input())
n = int(input())
res = sum((int(a) * int(b) for a, b in (input().split() for _ in range(n))))
print("Yes" if res == x else "No")