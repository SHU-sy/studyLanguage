import sys
import math
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    print(math.lcm(*map(int, input().split())))