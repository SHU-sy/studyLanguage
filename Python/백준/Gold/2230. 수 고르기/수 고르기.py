import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)])
l = 0
r = 0
min_num = 2000000001

if m == 0:
    print(0)
else:
    while r < n:
        current = arr[r] - arr[l]
        if current >= m:
            min_num = min(min_num, current)
            l += 1

        else:
            r += 1
    print(0 if min_num==2000000001 else min_num)