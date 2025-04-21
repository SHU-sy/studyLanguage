import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lans = [int(input()) for _ in range(k)]

start = 1
end = max(lans)
result = 0

while start <= end:
    mid = (start + end) // 2
    count = sum(lan // mid for lan in lans)

    if count >= n:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)