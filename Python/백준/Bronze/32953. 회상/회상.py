import sys
input = sys.stdin.readline

counter = dict()

n, m = map(int, input().split())
for _ in range(n):
    k = int(input())
    temp = list(map(int, input().split()))
    for key in temp:
        if key in counter:
            counter[key] += 1
        else:
            counter[key] = 1

count = 0
for key in counter:
    if counter[key] >= m:
        count += 1
print(count)