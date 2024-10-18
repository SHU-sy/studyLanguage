import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
num = [int(input().strip()) for _ in range(n)]
sort_num = sorted(num)
num_count = defaultdict(int)

for nums in num:
    num_count[nums] += 1

max_value = max(num_count.values())
max_keys = [key for key, value in num_count.items() if value == max_value]

avg = round(sum(num)/n, 0)
print(0 if avg == 0 else int(avg))
print(sort_num[n//2])

if len(max_keys) > 1:
    print(sorted(max_keys)[1])
else:
    print("".join(map(str, max_keys)))

print(sort_num[-1] - sort_num[0])