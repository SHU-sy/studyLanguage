import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

arr_sum = [0] * (n+1)
for i in range(1, n+1, 1):
    arr_sum[i] = arr_sum[i-1] + arr[i-1]

for _ in range(m):
    i, j = map(int, input().split())
    ans = arr_sum[j] - arr_sum[i-1]
    print(ans)