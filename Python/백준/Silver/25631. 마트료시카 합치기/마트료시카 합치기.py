import sys
from collections import defaultdict
input = sys.stdin.readline

dolls = defaultdict(int)
n = int(input())
arr = map(int, input().split())

for doll in arr:
    dolls[doll] += 1

print(max(dolls.values()))