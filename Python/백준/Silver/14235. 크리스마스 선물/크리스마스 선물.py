import sys
import heapq
input = sys.stdin.readline
res = []

n = int(input())
presents = []
for _ in range(n):
    a, *information = list(map(int, input().split()))

    if a == 0:
        if presents:
            res.append(-heapq.heappop(presents))
        else:
            res.append(-1)

    else:
        for present in information:
            heapq.heappush(presents, -present)

print("\n".join(map(str, res)))