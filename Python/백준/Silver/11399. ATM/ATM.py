import sys
input = sys.stdin.readline

n = input().strip()
min = map(int, input().split())
s_min = sorted(min)
total_min = 0
ans = []

for minute in s_min:
    total_min += minute
    ans.append(total_min)
print(sum(ans))