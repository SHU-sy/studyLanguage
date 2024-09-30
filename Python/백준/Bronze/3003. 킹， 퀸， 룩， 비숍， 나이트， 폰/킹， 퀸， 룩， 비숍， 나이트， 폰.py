import sys
a = list(map(int, sys.stdin.readline().split()))
b = [1, 1, 2, 2, 2, 8]
print(" ".join(map(str, [b - a for a, b in zip(a, b)])))