import sys
input = sys.stdin.readline
country = []

n, k = map(int, input().split())
for _ in range(n):
    country.append(list(map(int, input().split())))
country.sort(key=lambda x: (-x[1], -x[2], -x[3]))

rank = 1
same = 1
prev = country[0][1:]

ranking = {country[0][0] : rank}

for i in range(1, n):
    curr = country[i][1:]

    if curr == prev:
        ranking[country[i][0]] = rank
        same += 1
    else:
        rank += same
        same = 1
        ranking[country[i][0]] = rank
        prev = curr
print(ranking[k])