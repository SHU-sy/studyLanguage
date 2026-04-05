import sys
import heapq
input = sys.stdin.readline
res = []

n = int(input())
presents = []
for _ in range(n):
    information = list(map(int, input().split()))

    if information[0] == 0:
        if presents:
            res.append(-heapq.heappop(presents))
        else:
            res.append(-1)

    else:
        for present in information[1:]:
            heapq.heappush(presents, -present)

print("\n".join(map(str, res)))