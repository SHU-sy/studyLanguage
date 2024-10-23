import sys
from collections import defaultdict
input = sys.stdin.readline
n = int(input())
num_dict = defaultdict(int)
for _ in range(n):
    num_dict[int(input())] += 1

num_max = max(num_dict.values())
ans = [key for key, value in num_dict.items() if num_max == value]
print(sorted(ans)[0])