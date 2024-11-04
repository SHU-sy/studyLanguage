import sys
input = sys.stdin.readline

burger = [int(input()) for _ in range(3)]
coke = [int(input()) for _ in range(2)]

print(min(burger) + min(coke) - 50)