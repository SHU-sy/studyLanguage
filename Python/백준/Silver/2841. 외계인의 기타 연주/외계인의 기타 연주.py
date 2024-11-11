import sys
input = sys.stdin.readline

arr = [[] for _ in range(6)]
n, p = map(int, input().split())
count = 0

for _ in range(n):
    line, num = map(int, input().split())
    line -= 1

    while arr[line] and arr[line][-1] > num:
        arr[line].pop()
        count += 1

    if arr[line] and arr[line][-1] == num:
        continue

    arr[line].append(num)
    count += 1

print(count)