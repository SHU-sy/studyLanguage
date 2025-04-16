import sys
input = sys.stdin.readline

n = int(input())
best = input().strip()

for _ in range(n-1):
    name = input().strip()
    name_len = len(name)
    if name_len == 3:
        if len(best) > name_len or best > name:
            best = name
print(best)