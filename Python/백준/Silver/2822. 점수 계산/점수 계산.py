import sys
input = sys.stdin.readline

score = [int(input()) for _ in range(8)]
score_index = []
total_index = []
total_score = 0
for i in range(1, 9):
    score_index.append([score[i-1], i])
ans = sorted(score_index, key=lambda x: -x[0])[:5]

for score in ans:
    total_score += score[0]
    total_index.append(score[1])
print(total_score)
print(" ".join(map(str, sorted(total_index))))