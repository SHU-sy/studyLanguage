import sys
input = sys.stdin.readline
n = int(input())

stick = [int(input().strip()) for _ in range(n)]
stick.reverse()
temp = 0
count = 0

for length in stick:
    if length > temp:
        count += 1
        temp = length

print(count)