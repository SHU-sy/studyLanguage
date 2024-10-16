import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.reverse()

arr0 = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if arr[j] < arr[i]:
            arr0[i] = max(arr0[i], arr0[j] + 1)
print(n-max(arr0))
