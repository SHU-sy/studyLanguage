import sys
input = sys.stdin.readline

n = int(input())
num = sorted(set(map(int, input().split())))
print(" ".join(map(str, num)))