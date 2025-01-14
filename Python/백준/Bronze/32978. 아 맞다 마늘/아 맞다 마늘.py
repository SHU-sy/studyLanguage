import sys
input = sys.stdin.readline

n = int(input())
a = set(input().split())
b = set(input().split())
print("".join(a-b))