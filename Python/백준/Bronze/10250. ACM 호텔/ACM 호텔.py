import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    f = n%h
    if n % h == 0:
        f = h
    print(f"{f}{(n-1)//h+1:02}")