import sys
from collections import defaultdict
input = sys.stdin.readline

counter = defaultdict(int)

n, m = map(int, input().split())
for _ in range(n):
    k = int(input())
    temp = list(map(int, input().split()))
    for key in temp:
        counter[key] += 1

count = 0
for key in counter:
    if counter[key] >= m:
        count += 1
print(count)