import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    if n % h == 0:
        print(f"{h}{(n-1)//h+1:02}")
        continue
    print(f"{n % h}{(n-1)//h+1:02}")