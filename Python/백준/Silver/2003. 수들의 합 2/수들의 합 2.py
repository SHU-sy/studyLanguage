import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr_sum = [0] * (n + 1)
for i in range(1, n + 1):
    arr_sum[i] = arr_sum[i - 1] + arr[i - 1]

count = 0
s = 0
e = 1

while e <= n:
    section = arr_sum[e] - arr_sum[s]
    if section == m:
        count += 1
        s += 1
    elif section < m:
        e += 1
    else:
        s += 1
        if s == e:
            e += 1
print(count)