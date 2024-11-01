import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
n = int(input())
max_score = 0

for _ in range(n):
    score = 0
    for _ in range(3):
        a1, b1, c1 = map(int, input().split())
        score += (a1*a) + (b1*b) + (c1*c)
        max_score = max(max_score, score)
print(max_score)