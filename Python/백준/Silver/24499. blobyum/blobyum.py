import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = list(map(int, input().split()))
current_sum = sum(arr[:k])
max_taste = current_sum

for i in range(1, n):
    current_sum = current_sum - arr[i - 1] + arr[(i + k - 1) % n]
    max_taste = max(max_taste, current_sum)
print(max_taste)