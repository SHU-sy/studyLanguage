import sys
from collections import defaultdict
input = sys.stdin.readline
fruit_count = defaultdict(int)

n = int(input())
for _ in range(n):
    fruit, count = input().split()
    fruit_count[fruit] += int(count)

if any(count == 5 for count in fruit_count.values()):
    print("YES")
else:
    print("NO")