import sys
from collections import defaultdict
input = sys.stdin.readline
n = int(input())
num_dict = defaultdict(int)
for _ in range(n):
    num_dict[int(input())] += 1

ans = sorted(num_dict.items(), key=lambda item: (-item[1], item[0]))

print(ans[0][0])