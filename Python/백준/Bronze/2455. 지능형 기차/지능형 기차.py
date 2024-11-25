import sys
input = sys.stdin.readline
total = 0
max_people = 0

for _ in range(4):
    data = list(map(int, input().split()))
    total = total-data[0]+data[1]
    max_people = max(max_people, total)
print(max_people)