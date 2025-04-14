import sys
input = sys.stdin.readline

n = int(input())
num = sorted([int(input()) for _ in range(n)])
print(*num, sep="\n")