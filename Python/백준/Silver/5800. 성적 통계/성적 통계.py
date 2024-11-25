import sys
input = sys.stdin.readline

k = int(input())

for i in range(1, k+1, 1):
    data = list(map(int, input().split()))
    n = data[0]
    score = sorted(data[1:], reverse=True)
    largest_gap = max(score[j] - score[j + 1] for j in range(len(score) - 1))

    print(f"Class {i}")
    print(f"Max {score[0]}, Min {score[-1]}, Largest gap {largest_gap}")