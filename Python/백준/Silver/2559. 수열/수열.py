import sys
input = sys.stdin.readline

def tem_sum(n, k, arr):
    current_sum = sum(arr[:k])
    max_sum = current_sum

    for i in range(k, n):
        current_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, current_sum)
    return max_sum

n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(tem_sum(n, k, arr))