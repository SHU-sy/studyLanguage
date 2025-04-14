import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    score = list(map(int, input().split()))
    s = sorted(score)[1:4]
    print("KIN" if s[-1] - s[0] >= 4 else sum(s))