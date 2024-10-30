import sys
from collections import defaultdict
input = sys.stdin.readline
files = defaultdict(int)
n = int(input())

for _ in range(n):
    name, file = input().strip().split(".")
    files[file] += 1
for key in sorted(files.keys()):
    print(f"{key} {files[key]}")