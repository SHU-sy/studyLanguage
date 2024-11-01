import sys
from collections import defaultdict
input = sys.stdin.readline

n, c = map(int, input().split())
nums = list(map(int, input().split()))
num_count = defaultdict(int)
num_index = {}

for index, num in enumerate(nums):
    num_count[num] += 1
    if num not in num_index:
        num_index[num] = index

s_num = sorted(nums, key=lambda x: (-num_count[x], num_index[x]))
print(" ".join(map(str, s_num)))