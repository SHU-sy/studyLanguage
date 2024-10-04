import sys
input = sys.stdin.readline

n, m = map(int, input().split())
number = list(map(int, input().split()))
s = [0] * n  # prefix_sum
s[0] = number[0]
c = [0] * m  # same index count
count = 0  # 구간의 개수

for i in range(1, n):
    s[i] = s[i-1] + number[i]

for i in range(n):
    remainder = s[i] % m
    if remainder == 0:
        count += 1
    c[remainder] += 1

for i in range(m):
    if c[i] > 1:  # same index > 1
        count += c[i] * (c[i] - 1) // 2

print(count)