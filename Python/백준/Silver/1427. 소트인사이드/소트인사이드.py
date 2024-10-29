import sys
input = sys.stdin.readline

n = input().strip()
num = list(map(int, n))
print("".join(map(str, sorted(num, reverse=True))))