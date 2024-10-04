import sys
input = sys.stdin.readline
n, m = map(int, input().split())
number = list(map(int, input().split()))
temp = 0
prefix_sum = [0]

for i in number:  # partial sum
    temp = temp + i
    prefix_sum.append(temp)

for _ in range(m):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s - 1])