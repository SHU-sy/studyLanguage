import sys
from bisect import bisect_left
input = sys.stdin.readline

n, m = map(int, input().split())
arr1 = [int(input()) for _ in range(n)]
arr2 = sorted(arr1)
arr2_len = len(arr2)

for _ in range(m):
    quiz = int(input())
    index = bisect_left(arr2, quiz)

    if index < arr2_len and arr2[index] == quiz:
        print(index)
    else:
        print(-1)