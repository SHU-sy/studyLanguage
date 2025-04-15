import sys
input = sys.stdin.readline

n = int(input())
members = [(input().split()) for _ in range(n)]

best = members[0]

for member in members[1:]:
    current_score = int(member[1])
    best_score = int(best[1])
    if best_score < current_score or (best_score==current_score and best[0] > member[0]):
        best = member

print(best[0])