import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
s = 0
e = n -1
count = 0

while s < e:
    mem_sum = arr[s] + arr[e]
    if mem_sum < m:
        s += 1
    else:
        count += 1
        s += 1
        e -= 1
print(count)