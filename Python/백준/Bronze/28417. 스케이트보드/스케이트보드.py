import sys
input = sys.stdin.readline

n = int(input())
scores = []

for _ in range(n):
    score = list(map(int, input().split()))
    run, trick = score[0:2], score[2:7]
    max_trick = sorted(trick, reverse=True)[:2]
    scores.append(max(run) + sum(max_trick))
print(max(scores))