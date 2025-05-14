import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    cloth = defaultdict(int)
    temp = 1

    for _ in range(n):
        _, type = input().split()
        cloth[type] += 1

    for _, count in cloth.items():
        temp *= (count+1)
    print(temp -1)