import sys
input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))

arr_sum = [0] * (n + 1)
for i in range(1, n + 1):
    arr_sum[i] = arr_sum[i - 1] + arr[i - 1]

start = 0
end = 0
length = n+1

while end < n:
    section = arr_sum[end+1] - arr_sum[start]
    if section >= s:
        length = min(length, end-start+1)
        start += 1
    else:
        end += 1
print(length if length!=n+1 else 0)