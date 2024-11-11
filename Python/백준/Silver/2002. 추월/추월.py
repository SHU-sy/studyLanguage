import sys
input = sys.stdin.readline

n = int(input())
enter = [input().strip() for _ in range(n)]

count = 0
for _ in range(n):
    car = input().strip()
    if enter[0] != car:
        count += 1
    enter.remove(car)
print(count)