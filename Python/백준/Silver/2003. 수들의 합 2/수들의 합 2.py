import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr_sum = 0
count_arr = defaultdict(int)
count = 0

for num in arr:
    arr_sum += num

    if arr_sum == m:
        count += 1

    count += count_arr[arr_sum - m]
    count_arr[arr_sum] += 1

print(count)