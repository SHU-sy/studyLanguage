import sys
input = sys.stdin.readline

n, l = map(int, input().split())
h = sorted(list(map(int, input().split())))

for height in h:
    if height > l:
        break
    l += 1
print(l)