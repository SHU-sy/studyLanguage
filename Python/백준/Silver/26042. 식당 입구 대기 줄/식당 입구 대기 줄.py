import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
stu = deque()
res = []

for _ in range(n):
    infor = list(map(int, input().split()))

    if infor[0] == 1:
        stu.append(infor[1])
    else :
        stu.popleft()

    if stu:
        res.append((len(stu), stu[-1]))

result = sorted_res = sorted(res, key=lambda x: (-x[0], x[1]))[0]
print(f"{result[0]} {result[1]}")