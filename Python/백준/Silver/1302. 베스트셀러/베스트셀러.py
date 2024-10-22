import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
best_dict = defaultdict(int)

for _ in range(n):
    best_dict[input().strip()] += 1

max_count = max(best_dict.values())
candidates = [key for key, value in best_dict.items() if value == max_count]

print(sorted(candidates)[0])