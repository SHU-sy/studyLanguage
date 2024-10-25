import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = sorted(list(map(int, input().split())))

s = 0
e = len(arr)-1
count = 0

while s < e:
    if arr[s] + arr[e] > m:
        e -= 1
    elif arr[s] + arr[e] < m:
        s += 1
    else:
        count += 1
        s += 1
        e -= 1
print(count)