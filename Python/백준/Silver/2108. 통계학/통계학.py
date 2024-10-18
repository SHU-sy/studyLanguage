import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
num = [int(input().strip()) for _ in range(n)]
sort_num = sorted(num)
num_count = Counter(num)

avg = round(sum(num) / n)
print(int(avg))

print(sort_num[n // 2])

max_value = max(num_count.values())
max_keys = [key for key, value in num_count.items() if value == max_value]
print(sorted(max_keys)[1] if len(max_keys) > 1 else max_keys[0])

print(sort_num[-1] - sort_num[0])