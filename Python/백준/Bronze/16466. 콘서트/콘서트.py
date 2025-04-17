import sys
input = sys.stdin.readline

n = int(input())
tickets = set(map(int, input().split()))

for i in range(1, 1000000, 1):
    if i not in tickets:
        print(i)
        break