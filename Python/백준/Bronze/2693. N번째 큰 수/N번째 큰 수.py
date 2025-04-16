import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    number = sorted(map(int, input().split()), reverse=True)
    print(number[2])