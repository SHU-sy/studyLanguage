import sys
input = sys.stdin.readline

n = int(input())
ropes = sorted([int(input()) for _ in range(n)])
max_weight = 0
for i in range(n):
    max_weight = max((ropes[i]*(n-i)), max_weight)
print(max_weight)