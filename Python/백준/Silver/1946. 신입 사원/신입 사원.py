import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    count = 0
    people = [tuple(map(int, input().split())) for _ in range(n)]

    people.sort()
    max_score = 100001

    for a, b in people:
        if b < max_score:
            count += 1
            max_score = b
    print(count)