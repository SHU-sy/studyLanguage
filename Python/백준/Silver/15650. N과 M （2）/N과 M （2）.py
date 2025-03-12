import sys
input = sys.stdin.readline


def solution(v, d):
    if d + 1 == m:
        print(*arr)
    else:
        for i in range(v + 1, n+1):
            arr[d + 1] = i
            solution(i, d + 1)


n, m = map(int, input().split())
arr = [0 for i in range(0,m)]
for i in range(1, n + 1):
    if (n - m + 1 < i):
        break
    arr[0] = i
    solution(i, 0)