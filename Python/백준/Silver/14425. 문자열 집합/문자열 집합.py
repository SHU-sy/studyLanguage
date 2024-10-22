import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s_set = set()
for i in range(n):
    s_set.add(input().strip())

count = 0
for i in range(m):
    if input().strip() in s_set:
        count += 1
print(count)